def words(*args, separator="."):
    return separator.join(args)


print(words("沖縄県", "糸満市", "糸満", "1356-1", separator="_"))
print(words("home", "ProgrammingI_git", "ProgrammingI", "CHAPTER04", separator="/"))
