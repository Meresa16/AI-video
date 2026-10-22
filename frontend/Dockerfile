FROM node:20-alpine\n\nWORKDIR /app\n\nCOPY package.json package-lock.json* ./\nRUN npm ci || npm install\n\nCOPY . .\n\nEXPOSE 3000\n\nCMD [\
npm\, \run\, \dev\]
