# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/11/15
# Uses nested loops to print out RGB colour values


def main():
    # Title
    print("\n")
    print("RGB colour values \n")

    red = 0
    green = 0
    blue = 0
    # Print out the red RGB colour values
    while red <= 255:
        # Print out the green RGB colour values
        while green < 255:
            # Print out the blue RGB colour values
            while blue < 255:
                print(
                    "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                        str(red),
                        str(green),
                        str(blue),
                        "RGB(" + str(red) + "," + str(green) + "," + str(blue) + ")",
                    )
                )
                blue = blue + 1
            print(
                "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                    str(red),
                    str(green),
                    str(blue),
                    "RGB(" + str(red) + "," + str(green) + "," + str(blue) + ")",
                )
            )
            green = green + 1
        print(
            "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                str(red),
                str(green),
                str(blue),
                "RGB(" + str(red) + "," + str(green) + "," + str(blue) + ")",
            )
        )
        red = red + 1


if __name__ == "__main__":
    main()
