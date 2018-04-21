from datetime import datetime

def main():
    print_banner()
    input('Hit <enter> to start the stopwatch.')
    start_time = datetime.today()
    input('Hit <enter> to stop the stopwatch.')
    stop_time = datetime.today()
    elapsed_time = stop_time - start_time

    print(f'{elapsed_time} has passed.')

def print_banner():
    print('--------------------------------------')
    print('             STOPWATCH')
    print('--------------------------------------')


if __name__ == '__main__':
    main()