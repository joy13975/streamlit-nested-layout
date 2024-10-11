from typing import cast, Optional

from streamlit import cursor
from streamlit.delta_generator import DeltaGenerator
from streamlit.delta_generator import _enqueue_message
from streamlit.elements.form import FormData, current_form_id
from streamlit.proto import Block_pb2, ForwardMsg_pb2
from streamlit.runtime import caching

def _nestable_block(
    self,
    block_proto: Block_pb2.Block = Block_pb2.Block(),
    dg_type: Optional[type] = None,
) -> DeltaGenerator:
    # Operate on the active DeltaGenerator, in case we're in a `with` block.
    dg = self._active_dg

    # Prevent nested columns & expanders by checking all parents.
    block_type = block_proto.WhichOneof("type")
    # Convert the generator to a list, so we can use it multiple times.
    ancestor_block_types = list(dg._ancestor_block_types)
    # _check_nested_element_violation(self, block_type, ancestor_block_types)

    if dg._root_container is None or dg._cursor is None:
        return dg

    msg = ForwardMsg_pb2.ForwardMsg()
    msg.metadata.delta_path[:] = dg._cursor.delta_path
    msg.delta.add_block.CopyFrom(block_proto)

    # Normally we'd return a new DeltaGenerator that uses the locked cursor
    # below. But in this case we want to return a DeltaGenerator that uses
    # a brand new cursor for this new block we're creating.
    block_cursor = cursor.RunningCursor(
        root_container=dg._root_container,
        parent_path=dg._cursor.parent_path + (dg._cursor.index,),
    )

    # `dg_type` param added for st.status container. It allows us to
    # instantiate DeltaGenerator subclasses from the function.
    if dg_type is None:
        dg_type = DeltaGenerator

    block_dg = cast(
        DeltaGenerator,
        dg_type(
            root_container=dg._root_container,
            cursor=block_cursor,
            parent=dg,
            block_type=block_type,
        ),
    )
    # Blocks inherit their parent form ids.
    # NOTE: Container form ids aren't set in proto.
    block_dg._form_data = FormData(current_form_id(dg))

    # Must be called to increment this cursor's index.
    dg._cursor.get_locked_cursor(add_rows_metadata=None)
    _enqueue_message(msg)

    caching.save_block_message(
        block_proto,
        invoked_dg_id=self.id,
        used_dg_id=dg.id,
        returned_dg_id=block_dg.id,
    )

    return block_dg
DeltaGenerator._block = _nestable_block
