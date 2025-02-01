# solution to bouncing balls
# https://www.codewars.com/kata/5544c7a5cb454edb3c000047

def bouncing_ball(h, bounce, window):
    if h > 0 and (0 < bounce < 1) and window < h:
        view_count = 1
        h *= bounce
        while h > window:
            view_count += 2
            h *= bounce
        return view_count
    else:
        return -1


print(bouncing_ball(30, 0.75, 1.5))
