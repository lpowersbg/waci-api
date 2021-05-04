from waitress import serve
import waci

serve(waci.app, host='0.0.0.0', port=80)