import sys

if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("仮想環境がアクティブです。")
else:
    print("仮想環境はアクティブではありません。")
