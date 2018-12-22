# file-server
A simple web app used to visited files saved in filer server.

### framework

- flask
- jinja2
- bootstrap3

### Usage

1. You first to chane the directory path that  you wanted to visit.

   ```python
   # in file_server.py line 7
   # change the dir with your directory
   Base_Dir = 'D:\\data\\小项目\\file server\\files'
   ```

2. You may want to change username and password.

   ```python
   # in file_server.py line 32
   if name == 'zhazha' and pwd == 'zhazha':
       # ...
   ```

3. You can change server host or port.

   ```python
   # in file_server.py line 74
   app.run(port=9527, debug=False, host='0.0.0.0')
   ```

4. Start server

   ```python
   python ./file_server.py
   ```

5. Visited


