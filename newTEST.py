import subprocess

# 定义命令
command = ['scancode', '--license', '--html', 'D:/TestScan/test', 'D:/TestScan/requests']

try:
    # 执行命令
    result = subprocess.run(command, capture_output=True, text=True, check=True)

    # 打印命令输出
    print("Command Output:")
    print(result.stdout)

except subprocess.CalledProcessError as e:
    # 打印错误信息
    print("Command failed with error:")
    print(e.stderr)
    print("Return code:", e.returncode)
