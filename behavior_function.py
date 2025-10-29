import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# ============================================
# 1. RANDOM DELAYS - Humans don't act instantly
# ============================================

def human_delay(min_seconds=1, max_seconds=3):
    """Random delay between actions"""
    time.sleep(random.uniform(min_seconds, max_seconds))

def random_short_delay():
    """Very short random delay (0.5-1.5 seconds)"""
    time.sleep(random.uniform(0.5, 1.5))

def random_long_delay():
    """Longer random delay (3-7 seconds)"""
    time.sleep(random.uniform(3, 7))


# ============================================
# 2. HUMAN-LIKE SCROLLING
# ============================================

def human_scroll(driver, scrolls=3):
    """Scroll like a human - not to exact positions"""
    for i in range(scrolls):
        # Random scroll distance (not always to bottom)
        scroll_distance = random.randint(300, 800)
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        
        # Random pause between scrolls
        time.sleep(random.uniform(1, 3))
        
        # Sometimes scroll back up a bit (humans do this)
        if random.random() > 0.7:  # 30% chance
            scroll_back = random.randint(50, 150)
            driver.execute_script(f"window.scrollBy(0, -{scroll_back});")
            time.sleep(random.uniform(0.5, 1.5))

def smooth_scroll_to_element(driver, element):
    """Smoothly scroll to an element"""
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", 
        element
    )
    human_delay(1, 2)


# ============================================
# 3. HUMAN-LIKE MOUSE MOVEMENTS
# ============================================

def human_click(driver, element):
    """Click with random mouse movement"""
    actions = ActionChains(driver)
    
    # Move to element with pause
    actions.move_to_element(element).pause(random.uniform(0.1, 0.3))
    
    # Sometimes move away and back (humans adjust)
    if random.random() > 0.7:
        actions.move_by_offset(
            random.randint(-5, 5), 
            random.randint(-5, 5)
        ).pause(random.uniform(0.1, 0.2))
        actions.move_to_element(element).pause(random.uniform(0.1, 0.2))
    
    # Click
    actions.click().perform()
    random_short_delay()


def move_mouse_randomly(driver):
    """Move mouse to random positions (simulate reading)"""
    actions = ActionChains(driver)
    for _ in range(random.randint(2, 4)):
        x_offset = random.randint(-100, 100)
        y_offset = random.randint(-100, 100)
        actions.move_by_offset(x_offset, y_offset).pause(random.uniform(0.3, 0.8))
    actions.perform()

def act_like_human(driver, duration_seconds=30):
    """
    Make the browser act like a human is using it!
    
    Args:
        driver: Your Selenium WebDriver
        duration_seconds: How long to act human (default 30 seconds)
    
    Usage:
        act_like_human(driver)  # Acts human for 30 seconds
        act_like_human(driver, 60)  # Acts human for 60 seconds
    """
    
    print(f"🤖 Acting like a human for {duration_seconds} seconds...")
    
    start_time = time.time()
    action_count = 0
    
    while time.time() - start_time < duration_seconds:
        # Randomly choose what to do
        action = random.choice([
            'scroll_down',
            'scroll_up', 
            'scroll_little',
            'move_mouse',
            'pause',
            'scroll_to_top',
            'scroll_to_bottom'
        ])
        
        if action == 'scroll_down':
            # Scroll down a random amount
            scroll_amount = random.randint(200, 600)
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            print(f"⬇️  Scrolled down {scroll_amount}px")
            
        elif action == 'scroll_up':
            # Scroll up a random amount
            scroll_amount = random.randint(100, 400)
            driver.execute_script(f"window.scrollBy(0, -{scroll_amount});")
            print(f"⬆️  Scrolled up {scroll_amount}px")
            
        elif action == 'scroll_little':
            # Small scroll (reading)
            scroll_amount = random.randint(50, 150)
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            print(f"📖 Small scroll {scroll_amount}px")
            
        elif action == 'move_mouse':
            # Move mouse randomly
            actions = ActionChains(driver)
            for _ in range(random.randint(2, 5)):
                x = random.randint(-200, 200)
                y = random.randint(-200, 200)
                actions.move_by_offset(x, y)
                actions.pause(random.uniform(0.2, 0.5))
            actions.perform()
            print(f"🖱️  Moved mouse randomly")
            
        elif action == 'pause':
            # Just pause (reading/thinking)
            pause_time = random.uniform(2, 5)
            print(f"🤔 Pausing for {pause_time:.1f}s (reading...)")
            time.sleep(pause_time)
            continue  # Skip the normal delay
            
        elif action == 'scroll_to_top':
            # Scroll back to top
            driver.execute_script("window.scrollTo(0, 0);")
            print(f"🔝 Scrolled to top")
            
        elif action == 'scroll_to_bottom':
            # Scroll to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print(f"⬇️  Scrolled to bottom")
        
        action_count += 1
        
        # Random delay between actions
        delay = random.uniform(1, 4)
        time.sleep(delay)
    
    print(f"✅ Completed {action_count} human-like actions!")


# ============================================
# 4. HUMAN-LIKE TYPING
# ============================================

def human_type(element, text):
    """Type with random speed and occasional mistakes"""
    for char in text:
        element.send_keys(char)
        
        # Random typing speed (40-120 WPM equivalent)
        time.sleep(random.uniform(0.05, 0.2))
        
        # Occasional typo and correction (5% chance)
        if random.random() > 0.95:
            wrong_char = random.choice('abcdefghijklmnopqrstuvwxyz')
            element.send_keys(wrong_char)
            time.sleep(random.uniform(0.1, 0.3))
            element.send_keys(Keys.BACKSPACE)
            time.sleep(random.uniform(0.1, 0.2))
    
    # Sometimes pause at the end (thinking)
    if random.random() > 0.7:
        time.sleep(random.uniform(0.5, 1.5))


# ============================================
# 5. RANDOM BROWSER INTERACTIONS
# ============================================

def random_page_interaction(driver):
    """Perform random human-like interactions"""
    actions = [
        lambda: driver.execute_script(f"window.scrollBy(0, {random.randint(100, 300)});"),
        lambda: move_mouse_randomly(driver),
        lambda: driver.execute_script("window.scrollBy(0, -100);"),
        lambda: time.sleep(random.uniform(2, 4))  # Just pause (reading)
    ]
    
    # Do 1-2 random actions
    for _ in range(random.randint(1, 2)):
        random.choice(actions)()
        time.sleep(random.uniform(0.5, 1.5))


# ============================================
# 6. SETUP HUMAN-LIKE BROWSER
# ============================================

def setup_human_browser():
    """Configure Chrome to look more human"""
    options = webdriver.ChromeOptions()
    
    # Add realistic user agent
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    # Disable automation flags
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    # Look more like a real browser
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    
    # Create driver
    driver = webdriver.Chrome(options=options)
    
    # Remove webdriver property
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver


# ============================================
# 7. COMPLETE EXAMPLE - LINKEDIN COMMENTING
# ============================================

def scrape_with_human_behavior():
    """Example: Scrape and comment with human-like behavior"""
    
    driver = setup_human_browser()
    driver.get("https://www.linkedin.com/feed/")
    
    # Wait for page load (humans wait for page to load)
    random_long_delay()
    
    # Random mouse movements (like reading the page)
    move_mouse_randomly(driver)
    human_delay(2, 4)
    
    # Scroll like a human
    human_scroll(driver, scrolls=3)
    
    # Find posts
    content_list = driver.find_elements(By.CSS_SELECTOR, ".artdeco-card.mb2")
    
    # Don't comment on ALL posts (too suspicious)
    posts_to_comment = random.sample(
        range(len(content_list)), 
        min(random.randint(2, 5), len(content_list))
    )
    
    for index in posts_to_comment:
        content = content_list[index]
        
        try:
            # Scroll to post smoothly
            smooth_scroll_to_element(driver, content)
            
            # Sometimes just "read" the post without commenting
            if random.random() > 0.6:  # 40% chance to skip
                random_page_interaction(driver)
                continue
            
            # Highlight (for debugging)
            driver.execute_script(
                "arguments[0].style.border='3px solid green';", 
                content
            )
            
            # Find and click comment button (human-like)
            comment_button = content.find_element(
                By.CSS_SELECTOR,
                '.social-actions-button.comment-button'
            )
            human_click(driver, comment_button)
            human_delay(1, 2)
            
            # Wait for comment box
            comment_box = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.ql-editor'))
            )
            
            # Click to focus
            human_click(driver, comment_box)
            random_short_delay()
            
            # Type like a human
            comments = [
                "Great insights!",
                "Thanks for sharing this.",
                "Interesting perspective!",
                "Very helpful, appreciate it!"
            ]
            human_type(comment_box, random.choice(comments))
            
            # Remove highlight
            driver.execute_script(
                "arguments[0].style.border='';", 
                content
            )
            
            print(f"✅ Commented on post #{index + 1}")
            
            # Random delay before next action (humans don't spam)
            random_long_delay()
            
            # Sometimes do random interactions
            if random.random() > 0.7:
                random_page_interaction(driver)
            
        except Exception as e:
            print(f"⚠️ Skipped post #{index + 1}: {str(e)}")
            continue
    
    print(f"✅ Finished! Total posts: {len(content_list)}")
    
    # Don't close immediately (suspicious)
    human_delay(3, 6)
    driver.quit()


# ============================================
# 8. ADDITIONAL ANTI-DETECTION TIPS
# ============================================

"""
BEST PRACTICES FOR HUMAN-LIKE SCRAPING:

1. TIMING:
   - Random delays between actions (1-5 seconds)
   - Longer delays between major actions (3-10 seconds)
   - Don't scrape 24/7 - take breaks

2. PATTERNS:
   - Don't visit pages in exact order
   - Don't interact with every single element
   - Vary your behavior each session

3. RATE LIMITING:
   - Limit requests per minute
   - Take random breaks (5-15 minutes)
   - Vary session lengths

4. BROWSER:
   - Use realistic user agents
   - Rotate IP addresses if possible
   - Clear cookies periodically
   - Use residential proxies (not datacenter)

5. BEHAVIOR:
   - Scroll randomly (not just to bottom)
   - Move mouse occasionally
   - Type at human speeds
   - Sometimes "abandon" actions
   - Read content before interacting

6. DON'T:
   - Open 100 tabs at once
   - Click every button instantly
   - Scroll at exact same speed
   - Type at perfect speed
   - Run scripts 24/7
"""

# Run the example
if __name__ == "__main__":
    scrape_with_human_behavior()


def simulate_human_behavior(driver, num_actions=10):
    print("Simulating human-like behavior...")
    actions = ActionChains(driver)
    for _ in range(num_actions):
        scroll_y = random.randint(100, 800)
        driver.execute_script(f"window.scrollBy(0, {scroll_y});")
        time.sleep(random.uniform(0.5, 2))

    elements = driver.find_elements(By.CSS_SELECTOR, "div")
    for _ in range(num_actions):
        if elements:
            element = random.choice(elements)
            try:
                actions.move_to_element(element).pause(random.uniform(0.5, 2)).perform()
            except:
                pass
    print("Human-like actions completed.")
