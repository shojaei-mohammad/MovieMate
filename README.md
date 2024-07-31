# SubSync

SubSync is a user-friendly application that automatically renames subtitle files to match their corresponding movie files. It simplifies the process of organizing your media library by ensuring that subtitle filenames align with movie filenames.

## Features

- Intuitive graphical user interface
- Automatic matching of subtitle files to movie files
- Progress bar to track renaming process
- Real-time logging of operations
- Error handling and informative error messages

## Requirements

- Python 3.6 or higher
- tkinter (usually comes pre-installed with Python)

## Installation

1. Clone this repository or download the source code.
2. Navigate to the project directory.
3. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```
   python subsync.py
   ```
2. Click the "Select Directory" button and choose the folder containing your movie and subtitle files.
3. The application will automatically rename the subtitle files to match the movie files.
4. View the progress and any messages in the application window.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.