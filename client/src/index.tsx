import React from 'react'

import { createRoot } from 'react-dom/client'

import './index.css'

const container = document.getElementById('app-root')!
const root = createRoot(container)
root.render(<button
    onClick={ async() => 
    {
        const response = await fetch('/api/get_data')
        const json = await response.json()
        console.log(json)
    }
}
>Hello React!</button>)