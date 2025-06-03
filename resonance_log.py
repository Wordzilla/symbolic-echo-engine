# Logs echo strength, decay, and symbol integrity

def log_resonance(signal_strength, glyph_state):
    return {
        "resonance": signal_strength,
        "glyph_state": glyph_state,
        "status": "stable" if signal_strength > 0.75 else "fading"
    }
