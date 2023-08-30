<h1 align="center">
  <br>
  <br>
  A simple Yara Rule Generator written in Python.
  <br>
</h1>

#### Installation

Copy-paste this into your terminal:

```sh
git clone https://github.com/mkdirlove/yarules.git
```
```
cd yarules
```
```
python3 yarules.py -h
```
#### Usage

```
python3 yarules.py --rule-name AdvancedRule --strings '$my_string = "example" wide ascii\n$hex_string = { DE AD BE EF }' --string-count 2 --condition 'all of them'
```

#### Sample Yara Rule

```
rule SampleRule
{
    strings:
        $magic_string = "ThisIsASamplePattern"

    condition:
        $magic_string
}
```
