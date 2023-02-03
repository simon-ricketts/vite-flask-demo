# Vite Flask Demo


## Requirements

    node >=16.11
    python3.6

## Summary

This repo contains a `flask` backend and two examples of frontend design:

### browser-js

Based on traditional design practises, this demo is served entirely by browser compatible JavaScript code, with modules imported via `<script>` CDNs.

This frontend can be accessed by running the following command in `/flask`:

    make venv
    source venv/bin/activate
    python run_flask.py

and navigating to: http://127.0.0.1:5212

### vite

Based on modern Node.js design practises, this demo is served using `vite` which uses `Node.js` to import modules and transpile its code into browser compatible JavaScript.

##### Production Build

A production ready, static build can be accessed by running the following commands in order:

In `/vite`:

    npm ci
    npm run build

In `/flask`

    make venv
    source venv/bin/activate
    python run_flask.py --vite

and navigating to: http://127.0.0.1:5212

##### Dev Server

Alternatively, if you would lke to use `vite`'s local development server, run the following commands instead:

In `/vite`:

    npm ci
    npm run dev

In a seperate terminal, in `/flask`

    make venv
    source venv/bin/activate
    python run_flask.py

and navigate to: http://127.0.0.1:5173
