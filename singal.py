import asyncio
import serial_asyncio
import signal

async def read_serial_data(loop):
    reader, writer = await serial_asyncio.open_serial_connection(url='/dev/cu.usbserial-120', baudrate=9600)
    try:
        while True:
            line = await reader.read(100)  # 假设最多读取100字节的数据
            print(f"接收到的数据（16进制）: {line.hex()}")
    except asyncio.CancelledError:
        writer.close()
        await writer.wait_closed()
        print("串口读取任务被取消。")

def stop_program(loop):
    print("接收到终止信号，准备退出...")
    # 取消所有任务
    for task in asyncio.all_tasks(loop):
        task.cancel()
    print("所有任务请求取消。")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # 注册SIGINT信号的处理器
    loop.add_signal_handler(signal.SIGINT, stop_program, loop)
    # 运行主任务
    loop.run_until_complete(read_serial_data(loop))
    loop.close()
    print("事件循环已关闭，程序退出。")
