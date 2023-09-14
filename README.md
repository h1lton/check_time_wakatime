## Check time in wakatime
___
### Usage example:
```
C:\Users\username> wk
11 hrs 38 mins
```

The time displayed is accurate as on a dashboard, not as if you were using the wakatime cli or looking in PyCharm.

___

### What do you need to use this script?

- Python
- Add the path to the software dir to Path([example](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)) 
- or copy the wk.bat file to dir System32(Win + R > Enter system32)
- Open cmd and write `pip install requests`
- Open [main.py](main.py) and add your API Key.
- Verify that the script is working
```
PS I:\username\Desktop> wk
12 hrs 14 mins
```

### Update:

- #### version 2
    - добавил вывод последней сессии `01:42 - 01:47 | 0:04:49`.
    - Сессия - это список сигналов о том что вы пишите код в одном проекте, если разница между сигналами больше установлиного максимального кулдауна, сессия прерывается.

в планах или на параллельность посадить или на асинхронность

Если ничего не понятно, то сорян, делал специаньно для себя.
