# 驱动介绍
SYN6288中文语音合成芯片是北京宇音天下科技有限公司于2010年初推出的一款性价比更高，效果更自然的一款中高端语音合成芯片。虽然推出距今有十几年了，语音合成效果跟现代芯片对比也显得不那么自然，但并不妨碍它仍是一款比较优秀的语音合成芯片，对于初学者来说很有研究价值。
本驱动是基于micropython的SYN6288中文语音合成芯片驱动，使用它你可以轻松的进行语音合成、背景乐播放、提示音、和弦提示音以及和弦乐曲的播放。

## 开发初衷
虽然micropython相较C/C++有很多的不足，如运行速度慢、各种驱动库不足等，但仍不妨碍很多人（包括我）对于它的喜欢。最近在研究语音合成的时候，发现了SYN6288这款中文语音合成芯片，于是就想把它添加到我的项目中来。但是搜索github发现，并没有现成的基于micropython的驱动，只有C/C++的驱动。正在手足无错之际，通过查看SYN6288的datasheet以及Google检索，发现了一些解决方案，我对这些方案进行了整理，写出了这个驱动，分享给喜欢研究这款中文语音芯片的小伙伴们。
