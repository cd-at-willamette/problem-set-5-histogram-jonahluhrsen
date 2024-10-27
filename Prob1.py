from pgl import GWindow, GRect

#1a
def create_histogram_array(data:list[int])->list[int]:
    histogram = []
    for i in range(10):
        histogram.append(data.count(i))
    return histogram

#1b
def print_histogram(hist:list[int]) -> None:
    for i in range(10):
        print(f"{i}: {'*' * hist[i]}")

#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:

    gw = GWindow(width, height)

    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)
    # I needed help with chatgpt to get the graphic window working, had trouble with the x and y axis
    max_value = max(hist) if hist else 1 # https://docs.google.com/document/d/1SznzkLAk7rM_j6aumBTpj7HEU5FnhbQHIWgDw-KnmsM/edit?usp=sharing
    bar_width = width // len(hist)

    for i in range(10):
        rect_height = (hist[i] / max_value) * height
        y = height - rect_height
        my_rect(i * bar_width, y, bar_width, rect_height, 'red')

# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
print_histogram(hist) # uncomment to test
graph_histogram(hist, 400, 400) # uncomment to test



