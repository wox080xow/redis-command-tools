import sys
import subprocess
import logging

logger = logging.getLogger(__name__)

def shcmd(cmd):
    try:
        # 使用subprocess.run()執行shell命令，將標準輸出和標準錯誤輸出捕獲到變數中
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # 標準輸出保存到stdout變數中
        stdout = result.stdout.decode("utf-8")
        
        # 標準錯誤輸出保存到stderr變數中
        stderr = result.stderr.decode("utf-8")
        
        return stdout, stderr

    except subprocess.CalledProcessError as e:
        # 如果執行命令出錯，捕獲異常並打印錯誤信息
        
        # 沒有回傳值，加上FunctionTest的直接pass except，之後的函示就會收到"None type"
        # logger.debug(e)
        
        # 回傳錯誤／例外資訊
        return e
        
        # 在這就就跳出，就跑不到FunctionTest的try except了
        # sys.exit(1)
    
        