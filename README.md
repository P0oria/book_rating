# Book Rating

This Python script, named "Book Rating," allows users to rate different aspects of a book, providing an overall rating based on user input. Users are prompted to enter ratings on a scale of 0 to 5 for various criteria, allowing for a comprehensive evaluation of both fiction and non-fiction books.

## Functions

### `get_rating(category)`

This function is responsible for obtaining a rating from the user within the specified range of 0 to 5. It includes a provision for users to opt out of specific criteria by entering 0.

### `round_rating(rating)`

The `round_rating` function rounds a given rating to the nearest integer, taking into consideration the decimal part. If the decimal part is 0.5, the user is prompted for a more detailed impression to determine whether to round up or down.

### `main()`

The `main` function serves as the entry point of the program. It guides users through the process of rating different criteria based on the genre of the book (fiction or non-fiction). The criteria include aspects such as plot, characterization, writing style, accuracy, clarity, and more. The script then calculates and displays an overall rating, filtering out non-applicable (zero) ratings.

**Note: This script assumes that the user inputs the correct information, and defensive coding has been kept minimal to maintain simplicity.**

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/Book-Rating.git
   ```

2. **Navigate to the script directory:**

   ```bash
   cd Book-Rating
   ```

3. **Run the script:**

   - **On Mac:**
     ```bash
     python3 book_rating.py
     ```

   - **On PC:**
     ```bash
     python book_rating.py
     ```

4. **Enter 'f' for fiction or 'n' for non-fiction.**
5. **Rate various criteria based on the provided prompts.**
6. **Receive an overall rating for the book.**

## Rating Criteria

### Fiction (genre 'f')

- **Plot and Storyline:**
  - 1: Weak, lacks coherence and originality.
  - 5: Strong, well-developed, and original plot with unexpected twists.

- **Characterization:**
  - 1: Superficial characters with little depth or development.
  - 5: Complex, authentic characters with significant growth and evolution.

- **Writing Style:**
  - 1: Poorly crafted prose, difficult to follow.
  - 5: Engaging writing style, rich language, and effective pacing.

- **Themes and Messages:**
  - 1: Unclear or superficial themes.
  - 5: Profound and thought-provoking themes that resonate.

- **Impact and Enjoyment:**
  - 1: Fails to engage or leaves a negative impression.
  - 5: Highly impactful, enjoyable, and memorable.

### Non-Fiction (genre 'n')

- **Accuracy and Reliability:**
  - 1: Inaccurate information, unreliable sources.
  - 5: Highly accurate, well-researched content from credible sources.

- **Clarity and Accessibility:**
  - 1: Confusing, difficult to understand.
  - 5: Clear, accessible language for a wide audience.

- **Depth of Research:**
  - 1: Superficial research, lacking depth.
  - 5: Thorough research, extensive use of credible sources.

- **Relevance and Timeliness:**
  - 1: Outdated or irrelevant information.
  - 5: Timely, relevant, and applicable to current contexts.

- **Author's Perspective and Bias:**
  - 1: Strong, unacknowledged bias affecting objectivity.
  - 5: Transparent perspective, minimal bias, and balanced presentation.

## Output

The script provides an overall rating for the book based on the entered criteria. Feel free to use and modify this script to suit your book rating needs. Happy reading!
