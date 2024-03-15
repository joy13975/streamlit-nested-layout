# streamlit-nested-layout
An unofficial monkey patch that enables [streamlit](https://github.com/streamlit/streamlit) columns and expanders to be nested.

```diff
- ⚠️Streamlit developers disallow this behavior by design, so you are on your own if you encounter issues using this package!⚠️
```

Last tested for `streamlit==1.32.2` on `Python 3.9.18`.

Credits to [streamlit PR #5266](https://github.com/streamlit/streamlit/pull/5266) by [@ZeroCool940711](https://github.com/ZeroCool940711).

### Install
```
pip install streamlit-nested-layout
```

### Usage
Just import this package once in your app.

```
import streamlit_nested_layout
```

### Demo
![Demo](https://raw.githubusercontent.com/joy13975/streamlit-nested-layout/main/images/demo.png)