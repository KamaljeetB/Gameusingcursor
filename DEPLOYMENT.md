# 🌐 Deploy Labubu Obstacle Course Online

This guide will help you publish your Labubu game so friends can play it online!

## 🚀 **Option 1: Replit (Recommended - Easiest)**

### **Step 1: Create Replit Account**
1. Go to [replit.com](https://replit.com)
2. Sign up for a free account
3. Click "Create Repl"

### **Step 2: Upload Your Game**
1. Choose "Python" as the language
2. Give it a name like "Labubu-Obstacle-Course"
3. Upload all your game files (drag & drop)
4. Make sure these files are included:
   - `main.py`
   - `game/` folder
   - `config/` folder
   - `utils/` folder
   - `requirements.txt`

### **Step 3: Install Dependencies**
1. In the Replit shell, run:
   ```bash
   pip install -r requirements.txt
   ```

### **Step 4: Run & Share**
1. Click the "Run" button
2. Your game will start in the Replit console
3. Click "Share" to get a shareable URL
4. Send the URL to friends!

**✅ Pros:** Free, easy, works immediately
**❌ Cons:** Limited to Replit platform

---

## 🌐 **Option 2: GitHub Pages + Pygame-web**

### **Step 1: Convert Game to Web Format**
1. Install pygame-web:
   ```bash
   pip install pygame-web
   ```

2. Convert your game:
   ```bash
   pygame-web main.py
   ```

### **Step 2: Create GitHub Repository**
1. Create new repo on GitHub
2. Upload the converted web files
3. Enable GitHub Pages in settings

### **Step 3: Deploy**
1. Your game will be available at:
   `https://yourusername.github.io/reponame`

**✅ Pros:** Professional, permanent, custom domain possible
**❌ Cons:** More complex setup, requires conversion

---

## 🎮 **Option 3: Itch.io (Game Platform)**

### **Step 1: Create Itch.io Account**
1. Go to [itch.io](https://itch.io)
2. Sign up for free account

### **Step 2: Upload Game**
1. Click "Upload new project"
2. Upload your game files
3. Set price (free or paid)
4. Add screenshots and description

### **Step 3: Share**
1. Get your game page URL
2. Share with friends!

**✅ Pros:** Gaming community, professional platform
**❌ Cons:** Requires game packaging

---

## 🔧 **Quick Replit Setup (Step-by-Step)**

1. **Go to [replit.com](https://replit.com)**
2. **Click "Create Repl"**
3. **Select "Python"**
4. **Name it "Labubu-Game"**
5. **Upload your files:**
   ```
   📁 Labubu-Game/
   ├── main.py
   ├── game/
   ├── config/
   ├── utils/
   ├── requirements.txt
   └── .replit
   ```
6. **Click "Run"**
7. **Click "Share" to get URL**

## 🌟 **Your Game Features for Sharing:**

- 🦊 **Cute Labubu Character**
- 🎵 **Sound Effects & Music**
- ⏸️ **Pause System**
- 🪙 **Coin & Gem Collectibles**
- 🎯 **Increasing Difficulty**
- 🎮 **Simple Controls**

## 📱 **Mobile Compatibility:**

The game works best on desktop/laptop due to keyboard controls, but friends can play on any device with a keyboard!

---

## 🆘 **Need Help?**

If you run into issues:
1. Check the console for error messages
2. Make sure all files are uploaded
3. Verify requirements.txt is correct
4. Try refreshing the Replit page

**Your game is ready to go online! 🎉**
