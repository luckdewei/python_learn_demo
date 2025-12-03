import timeit


def test_performance():
    n = 10000

    # 列表推导式
    list_comp_time = timeit.timeit(
        "[x**2 for x in range(n)]", globals={"n": n}, number=1000
    )

    # 传统 for 循环
    for_loop_time = timeit.timeit(
        """
result = []
for x in range(n):
    result.append(x**2)
""",
        globals={"n": n},
        number=1000,
    )

    # 生成器表达式
    gen_expr_time = timeit.timeit(
        "list(x**2 for x in range(n))", globals={"n": n}, number=1000
    )

    print(f"列表推导式: {list_comp_time:.4f}秒")
    print(f"传统循环: {for_loop_time:.4f}秒")
    print(f"生成器表达式: {gen_expr_time:.4f}秒")


test_performance()
