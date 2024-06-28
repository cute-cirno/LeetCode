class FileSystem:
    def __init__(self):
        self.root = {}
        self.current_path = ['/']
        self.current_dir = self.root

    def mkdir(self, dirname):
        if dirname in self.current_dir:
            return  # 目录已存在，不执行任何操作
        self.current_dir[dirname] = {}

    def cd(self, dirname):
        if dirname == '..':
            if len(self.current_path) > 1:
                self.current_path.pop()
                self.current_dir = self.root
                for dir in self.current_path[1:]:
                    self.current_dir = self.current_dir[dir]
        elif dirname in self.current_dir:
            self.current_path.append(dirname)
            self.current_dir = self.current_dir[dirname]
        else:
            return  # 目录不存在，不执行任何操作

    def pwd(self):
        return '/' + '/'.join(self.current_path[1:])

    def execute_command(self, command):
        parts = command.split()
        if len(parts) == 0:
            return

        cmd = parts[0]
        if cmd == 'mkdir' and len(parts) == 2:
            self.mkdir(parts[1])
        elif cmd == 'cd' and len(parts) == 2:
            self.cd(parts[1])
        elif cmd == 'pwd' and len(parts) == 1:
            return self.pwd()
        else:
            return  # 无效命令，不执行任何操作

def manage_directory(commands):
    fs = FileSystem()
    last_output = None
    for command in commands:
        result = fs.execute_command(command)
        if result is not None:
            last_output = result
    return last_output

# 测试用例
commands = [
    "mkdir abc",
    "cd abc",
    "mkdir def",
    "cd def",
    "mkdir def",
    "cd def",
    "mkdir def",
    "cd def",
    "cd ..",
    "pwd"
]
print(manage_directory(commands))  # 输出: /abc/def
