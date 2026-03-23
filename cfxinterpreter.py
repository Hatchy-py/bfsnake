def interpret_extended_bf(code, grid_size=16):
    memory = [0] * 30000
    ptr = 0
    grid_start = 2 

    stack, loops = [], {}
    for i, char in enumerate(code):
        if char == '[': stack.append(i)
        elif char == ']':
            start = stack.pop()
            loops[start], loops[i] = i, start

    pc = 0
    while pc < len(code):
        cmd = code[pc]
        if   cmd == '>': ptr += 1
        elif cmd == '<': ptr -= 1
        elif cmd == '+': memory[ptr] = (memory[ptr] + 1) % 256
        elif cmd == '-': memory[ptr] = (memory[ptr] - 1) % 256
        elif cmd == 'v': ptr += grid_size
        elif cmd == '^': ptr -= grid_size
        elif cmd == '[' and memory[ptr] == 0: pc = loops[pc]
        elif cmd == ']' and memory[ptr] != 0: pc = loops[pc]
        pc += 1
      
    print("\n--- Grid 16x16 ---")
    for r in range(grid_size):
        row_str = ""
        for c in range(grid_size):
            idx = grid_start + (r * grid_size) + c
            row_str += "█" if memory[idx] > 200 else "░"
        print(row_str)

test_code = ">>" + "+" * 201 + "v" + "+" * 201
interpret_extended_bf(test_code)
