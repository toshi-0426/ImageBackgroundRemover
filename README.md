# Simple Image Background Remover
This is a program that allows users to remove the background of an image from images using the remove.bg API. 


## Description
Users can drag and drop image or select it from their file system. The processed images are then saved locally.
This is intended to use for your id photo. I created this for learning purpose.

## Prerequisites
- Python 3.10 or later
- A valid API key from remove.bg

## Installation
1. Run the following command:
    ```bash
    pip install -r requirement.txt
    ```
2. Set an API as an environment variable by implementing the following:
    ```bash
    export X-Api-Key="your_api_key_here"　　　#On Windows　　　set X-Api-Key=your_api_key_here
    ```

## Usage
1. Run the following command:
    ```bash
    pip install -r requirement.txt
    ```
2. Obtain an API key form [remove.bg](https://www.remove.bg/).
3. Set an API as an environment variable by implementing the following on terminal:
    ```bash
    export X-Api-Key="your_api_key_here"　　　#On Windows 'set X-Api-Key=your_api_key_here'
    ```
4. Run the program 
    ```bash
    python src/app.py
    ```
5. Use the application:
    - Drop an image file (JPEG or PNG) into the designated area.
    - Or upload it to choose it from your directry.
    - Click download button
    - Click cancel button to remove the selected image from the applicatoin


## LICENSE
Copyright (c) 2019 Brian Lam
[remove.bg](https://www.remove.bg/) is licensed under the MIT License.
A copy of the license can be found at [GitHub Pages](https://github.com/brilam/remove-bg/blob/master/LICENSE)