# Write up (Sharif University CTF 2016 : Android App)

flag : `Sharif_CTF{833489ef285e6fa80690099efc5d9c9d}`

## 一言Write up
MainActivityがlibadnjni.soをロードし，processObjectArrayFromNativeをインポートしている．
processObjectArrayFromNativeでハードコーディングされた文字列と比較している．

## Write up

