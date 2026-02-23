# dashboard/pages/app.py
import os
os.environ['CREWAI_TELEMETRY_OPT_OUT'] = '1'

# ---------- Patch signal.signal to ignore calls from non‑main threads ----------
import signal
import threading

_original_signal = signal.signal

def _patched_signal(sig, handler):
    if threading.current_thread() is threading.main_thread():
        return _original_signal(sig, handler)
    # In a non‑main thread, do nothing (return a dummy)
    return None

signal.signal = _patched_signal
# --------------------------------------------------------------------------------

import sys
from pathlib import Path
import streamlit as st

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from src.crew_setup import ResearchCrew

st.set_page_config(page_title="AI Research Assistant", page_icon="🔬")
st.title("🔬 AI Research Assistant (Full Agent Crew)")

topic = st.text_input("Enter a research topic:")
if st.button("Start Research") and topic:
    crew = ResearchCrew(topic=topic, context="", audience="General Public", format_type="Detailed Report")
    with st.spinner("Agents are working..."):
        result = crew.run()
    if result.get('success'):
        st.success("Research complete!")
        st.markdown(result['output'])
    else:
        st.error(f"Research failed: {result.get('error', 'Unknown error')}") # dashboard/pages/app.py
import os
os.environ['CREWAI_TELEMETRY_OPT_OUT'] = '1'

# ---------- Monkey‑patch to prevent signal handler registration ----------
import sys
import threading
import types

if threading.current_thread() is not threading.main_thread():
    dummy_telemetry = types.ModuleType('crewai.telemetry.telemetry')
    def dummy_init(self, *args, **kwargs): pass
    dummy_telemetry.Telemetry = type('Telemetry', (), {
        '__init__': dummy_init,
        'set_tracer': lambda *a, **kw: None,
        'crew_creation': lambda *a, **kw: None,
        'tool_creation': lambda *a, **kw: None,
        'agent_creation': lambda *a, **kw: None,
        'task_creation': lambda *a, **kw: None,
        'crew_execution_span': lambda *a, **kw: None,
        'end_span': lambda *a, **kw: None,
    })
    sys.modules['crewai.telemetry.telemetry'] = dummy_telemetry
# --------------------------------------------------------------------------

import streamlit as st
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from src.crew_setup import ResearchCrew

st.set_page_config(page_title="AI Research Assistant", page_icon="🔬")
st.title("🔬 AI Research Assistant (Full Agent Crew)")

topic = st.text_input("Enter a research topic:")
if st.button("Start Research") and topic:
    crew = ResearchCrew(topic=topic, context="", audience="General Public", format_type="Detailed Report")
    with st.spinner("Agents are working..."):
        result = crew.run()
    if result.get('success'):
        st.success("Research complete!")
        st.markdown(result['output'])
    else:
        st.error(f"Research failed: {result.get('error', 'Unknown error')}")