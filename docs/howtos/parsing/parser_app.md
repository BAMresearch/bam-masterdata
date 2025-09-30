# How-to: Use the Parser app

This how-to guide explains how to use the Parser app in your browser to upload files, run the parser, and transfer parsed metadata to the Data Store. It is intended for users who want a step-by-step walkthrough of the main app functions.

!!! note "Prerequisites"
    <!-- List here any prerequisites needed to deploy or understand the app (e.g., login credentials, access to Spaces, supported file formats). -->
    **WIP**

---

## Open and login in the app

<ol>
    <li>Open your web browser.</li>
    <li>Go to the provided URL of the Parser app (e.g., https://parser.example.com).</li>
    <li>The login page of the app will appear.</li>

    <div class="click-zoom">
        <label>
            <input type="checkbox">
            <img src="../../../assets/parsing/LoginParserApp.jpg" alt="Login in the Parser app." width="50%" title="Click to zoom in">
        </label>
    </div>

    <li>Enter your Username.</li>
    <li>Enter your Password.</li>
    <li>Press <b>Login</b>.</li>
</ol>


## Select and Upload Files
1. Select the Space where data will be saved.
2. Enter Project and Collection names.
3. Drag and drop or click to select files.
4. Press **Upload Files** to upload them.
    - Click the **Reset** button to start over if needed.

<div class="click-zoom">
    <label>
        <input type="checkbox">
        <img src="../../../assets/parsing/Card1ParserApp.jpg" alt="Card 1 in the Parser app." width="50%" title="Click to zoom in">
    </label>
</div>


## Select Parsers
1. Choose a parser by clicking **Select Parser** for each uploaded file.
    - Available parsers are listed in the corner.
    - See [How-to: Create new parsers](create_new_parsers.md) to create your own.
2. Press **Parse** to extract metadata from each file and upload it to the Data Store. The extraction is defined in the logic of each defined parser.

<div class="click-zoom">
    <label>
        <input type="checkbox">
        <img src="../../../assets/parsing/Card2.jpg" alt="Card 2 in the Parser app." width="50%" title="Click to zoom in">
    </label>
</div>

## Review Logs
1. Check logs to verify successful parsing. If parsing fails, check the logs and debug the parsing process.
2. If parsing works, only INFO messages will appear in the logs card.

<div class="click-zoom">
    <label>
        <input type="checkbox">
        <img src="../../../assets/parsing/Card3Logs.jpg" alt="Card 3 in the Parser app." width="50%" title="Click to zoom in">
    </label>
</div>
