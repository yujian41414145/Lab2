def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    user_input = input("Enter numbers: ")

    str_list = user_input.split(",")

    num_list = []
    for num in str_list:
        num_list.append(float(num))

    return num_list


def calc_average(temp_list):
    average = sum(temp_list) / len(temp_list)
    return average


def find_min_max(temp_list):
    min_temp = min(temp_list)
    max_temp = max(temp_list)
    return min_temp, max_temp


def sort_temperature(temp_list):
    print("sort_temperature")


def calc_median_temperature(temp_list):
    print("calc_median_temperature")


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

    display_main_menu()
    num_list = get_user_input()

    average = calc_average(num_list)
    min_temp, max_temp = find_min_max(num_list)

    print("Average Temperature =", f"{average:.2f}")
    print("Minimum Temperature =", f"{min_temp:.2f}")
    print("Maximum Temperature =", f"{max_temp:.2f}")


if __name__ == "__main__":
    main()
