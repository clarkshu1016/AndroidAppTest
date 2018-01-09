## Get App CPU Info

#### 1.检测CPU消耗情况
* On Windows:adb shell dumpsys cpuinfo | findstr com.google.android.youtube
* On MacOS/Linux: adb shell dumpsys cpuinfo | findstr com.google.android.youtube

```{r, engine='bash', count_lines}
adb shell dumpsys cpuinfo | findstr com.google.android.youtube
0.5% 30278/com.google.android.youtube: 0.3% user + 0.2% kernel / faults: 27 minor
```

