class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
```

Kodni ishlatib ko'rish uchun quyidagilarni amalga oshiring:

1. Kodni yozib, D klassini yaratib ko'ring.
2. D klassining mro() metodini chaqiring.
3. Natija: [__main__.D, __main__.B, __main__.C, __main__.A, object]
