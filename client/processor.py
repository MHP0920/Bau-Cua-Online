def _solve(_player: list, _server: list, _balance: int):
    for choice in set(_player):
        if choice in _server:
            _balance += 5 * _player.count(choice) * _server.count(choice)
        elif choice not in _server:
            _balance -= 5 * _player.count(choice)
    return _balance