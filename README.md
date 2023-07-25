# BypassFilterASP

Any transformation between the moment the request is received and the construction of the final HTML view can lead to filter bypass. If an HTTP parameter is URL decoded two times, it is enough to bypass the filter.

## Mode Use

```sh
usage: bypass.py [-h] -i INPUT_FILE -o OUTPUT_FILE
bypass.py: error: the following arguments are required: -i/--input_file, -o/--output_file
```

```sh
python3 bypass.py -i xss.txt -o resultados.tx

```

![image](https://github.com/HernanRodriguez1/BypassFilterASP/assets/66162160/51eb9e2b-2535-4ddf-8a3c-0030edfd2b86)

Based in: https://gosecure.github.io/presentations/2017-12-04-confoo/Bypassing%20Modern%20XSS%20Protections.pdf
