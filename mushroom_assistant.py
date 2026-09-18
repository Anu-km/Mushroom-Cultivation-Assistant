 
import tkinter as tk 
from tkinter import ttk, messagebox 
import datetime 
import random 
 
 
substrates = { 
    "Paddy Straw": { 
        "substrate": ["Paddy straw", "Banana leaves", "Sugarcane bagasse"], 
        "temp": "30–35°C", 
        "humidity": "80–90%", 
        "yield": "1.0 kg/kg", 
        "growth_days": 18, 
        "reason": "Locally available substrate, decomposes easily, and supports rapid growth." 
    }, 
    "Oyster": { 
        "substrate": ["Paddy straw", "Sugarcane bagasse", "Sawdust"], 
        "temp": "25–30°C", 
        "humidity": "85–90%", 
        "yield": "1.5 kg/kg", 
        "growth_days": 20, 
        "reason": "High cellulose content provides good nutrition for mycelium growth." 
    }, 
    "Milky": { 
        "substrate": ["Wheat straw", "Sugarcane bagasse"], 
        "temp": "30–35°C", 
        "humidity": "85–90%", 
        "yield": "1.3 kg/kg", 
        "growth_days": 22, 
        "reason": "Tolerant to tropical conditions and grows well on cellulose-rich substrate." 
    }, 
    "Button": { 
        "substrate": ["Composted manure", "Wheat straw"], 
        "temp": "18–22°C", 
        "humidity": "85–95%", 
        "yield": "1.2 kg/kg", 
        "growth_days": 25, 
        "reason": "Requires cooler climate and nutrient-rich compost for fruiting." 
    } 
} 
 
problems = { 
    "white mold": {"type": "Biotic", "suggestion": "Reduce humidity and sterilize substrate."}, 
    "insect infestation": {"type": "Biotic", "suggestion": "Use neem extract and maintain hygiene."}, 
    "slow growth": {"type": "Abiotic", "suggestion": "Increase temperature to 28–30°C and humidity to 85%."}, 
    "dry caps": {"type": "Abiotic", "suggestion": "Spray water lightly and maintain humidity."}, 
    "bad smell": {"type": "Biotic", "suggestion": "Contamination — discard batch and sterilize the area."} 
} 
 
 
def show_screening(): 
    mushroom = mushroom_var.get() 
    if mushroom in substrates: 
        data = substrates[mushroom] 
        start_date = datetime.date.today() 
        harvest_date = start_date + datetime.timedelta(days=data['growth_days']) 
 
        quantitative = ( 
            f"📊 Quantitative Data:\n" 
            f"- Expected Yield: {data['yield']}\n" 
            f"- Growth Days: {data['growth_days']}\n" 
            f"- Temperature: {data['temp']}\n" 
            f"- Humidity: {data['humidity']}\n" 
        ) 
        qualitative = ( 
            f"📝 Qualitative Data:\n" 
            f"- Reason for substrate choice: {data['reason']}\n" 
            f"- Suggested care: Keep temperature and moisture under control.\n" 
        ) 
 
        result = ( 
            f"🍄 {mushroom} Mushroom Screening\n" 
            f"Start Date: {start_date}\n" 
            f"Harvest Date: {harvest_date}\n\n" 
            f"Substrates: {', '.join(data['substrate'])}\n\n" 
            f"{quantitative}\n" 
            f"{qualitative}" 
        ) 
 
        screen_output.config(state='normal') 
        screen_output.delete(1.0, tk.END) 
        screen_output.insert(tk.END, result) 
        screen_output.config(state='disabled') 
    else: 
        messagebox.showwarning("Invalid Input", "Please select a valid mushroom type.") 
 
def solve_problem(): 
    symptom = symptom_entry.get().lower().strip() 
    if symptom in problems: 
        issue = problems[symptom] 
        result = ( 
            f"🧫 Problem: {symptom.title()}\n" 
            f"Type of Stress: {issue['type']} Stress\n" 
            f"💡 Suggestion: {issue['suggestion']}" 
        ) 
        problem_output.config(state='normal') 
        problem_output.delete(1.0, tk.END) 
        problem_output.insert(tk.END, result) 
        problem_output.config(state='disabled') 
    else: 
        messagebox.showinfo("Not Found", "Symptom not recognized. Try another description.") 
 
def show_market(): 
    mushroom = market_var.get() 
    prices = { 
        "Paddy Straw": random.randint(100, 160), 
        "Oyster": random.randint(150, 220), 
        "Milky": random.randint(180, 250), 
        "Button": random.randint(200, 260) 
    } 
    if mushroom in prices: 
        price = prices[mushroom] 
        suggestion = "📈 Sell now! Good demand." if price > 180 else "📉 Hold for better price." 
        result = ( 
            f"💰 {mushroom} Mushroom Market Info\n" 
            f"- Current Price: ₹{price}/kg\n" 
            f"- Recommendation: {suggestion}\n" 
            f"- Tip: Monitor market weekly for trends." 
        ) 
        market_output.config(state='normal') 
        market_output.delete(1.0, tk.END) 
        market_output.insert(tk.END, result) 
        market_output.config(state='disabled') 
    else: 
        messagebox.showwarning("Invalid Input", "Please select a mushroom type.") 
 
 
root = tk.Tk() 
root.title("🌾 MUSHROOM") 
root.geometry("750x700") 
root.configure(bg="#F0F4C3") 
root.resizable(False, False) 
 
# --- Title --- 
title = tk.Label(root, text="🌱  MUSHROOM CULTIVATION ASSISTANT  ",  
                 font=("Segoe UI Black", 26, "bold"), bg="#F0F4C3", fg="#33691E") 
title.pack(pady=10) 
 
# --- Notebook --- 
notebook = ttk.Notebook(root) 
notebook.pack(fill='both', expand=True, padx=15, pady=10) 
 
# ---------------- Tab 1: Screening ---------------- 
screen_tab = ttk.Frame(notebook) 
notebook.add(screen_tab, text="  Screening") 
 
frame_screen = tk.LabelFrame(screen_tab, text="Screening & Material Selection",  
                             font=("Segoe UI Semibold", 13, "bold"), padx=10, pady=10) 
frame_screen.pack(fill='both', expand=True, padx=15, pady=15) 
 
tk.Label(frame_screen, text="Select Mushroom Type:", font=("Verdana", 12, "bold")).grid(row=0, column=0, pady=5, sticky='w') 
mushroom_var = tk.StringVar(value="Paddy Straw") 
ttk.Combobox(frame_screen, textvariable=mushroom_var,  
             values=list(substrates.keys()), width=30, font=("Verdana", 11)).grid(row=0, column=1, pady=5) 
 
tk.Button(frame_screen, text="Show Screening Details", command=show_screening,  
          bg="#8BC34A", fg="black", width=25, font=("Verdana", 12, "bold")).grid(row=1, column=0, columnspan=2, pady=10) 
 
screen_output = tk.Text(frame_screen, height=12, width=80, bg="#F1F8E9", font=("Consolas", 11), wrap='word') 
screen_output.grid(row=2, column=0, columnspan=2, pady=10) 
screen_output.config(state='disabled') 
 
# ---------------- Tab 2: Problem Solver ---------------- 
problem_tab = ttk.Frame(notebook) 
notebook.add(problem_tab, text="Problem Solver") 
 
frame_problem = tk.LabelFrame(problem_tab, text="Problem Diagnosis & Solution",  
                              font=("Segoe UI Semibold", 13, "bold"), padx=10, pady=10) 
frame_problem.pack(fill='both', expand=True, padx=15, pady=15) 
 
tk.Label(frame_problem, text="Enter Symptom:", font=("Verdana", 12, "bold")).grid(row=0, column=0, pady=5, sticky='w') 
symptom_entry = tk.Entry(frame_problem, width=40, font=("Verdana", 11)) 
symptom_entry.grid(row=0, column=1, pady=5) 
 
tk.Button(frame_problem, text="Get Suggestion", command=solve_problem,  
          bg="#8BC34A", fg="black", width=25, font=("Verdana", 12, "bold")).grid(row=1, column=0, columnspan=2, pady=10) 
 
problem_output = tk.Text(frame_problem, height=12, width=80, bg="#FFF3E0", font=("Consolas", 11), wrap='word') 
problem_output.grid(row=2, column=0, columnspan=2, pady=10) 
problem_output.config(state='disabled') 
 
# ---------------- Tab 3: Market Info ---------------- 
market_tab = ttk.Frame(notebook) 
notebook.add(market_tab, text="Market Alert") 
 
frame_market = tk.LabelFrame(market_tab, text="Market Prices & Recommendations",  
                             font=("Segoe UI Semibold", 13, "bold"), padx=10, pady=10) 
frame_market.pack(fill='both', expand=True, padx=15, pady=15) 
 
tk.Label(frame_market, text="Select Mushroom Type:", font=("Verdana", 12, "bold")).grid(row=0, column=0, pady=5, sticky='w') 
market_var = tk.StringVar(value="Paddy Straw") 
ttk.Combobox(frame_market, textvariable=market_var,  
             values=list(substrates.keys()), width=30, font=("Verdana", 11)).grid(row=0, column=1, pady=5) 
 
tk.Button(frame_market, text="Show Market Info", command=show_market,  
          bg="#8BC34A", fg="black", width=25, font=("Verdana", 12, "bold")).grid(row=1, column=0, columnspan=2, pady=10) 
 
market_output = tk.Text(frame_market, height=12, width=80, bg="#E3F2FD", font=("Consolas", 11), wrap='word') 
market_output.grid(row=2, column=0, columnspan=2, pady=10) 
market_output.config(state='disabled') 
 
# ---------------- Run App ---------------- 
root.mainloop() 
