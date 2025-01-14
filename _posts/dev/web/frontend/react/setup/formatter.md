📍 **install**

```
npm install --save-dev prettier
```

📒 **.prettierrc.js**

```javascript
module.exports = {
    singleQuote: true,
    trailingComma: 'all',
    printWidth: 100,
};
```

📒 **package.json**

```json
  "scripts": {
		...
    "format:check": "prettier --check ./src",
    "format:fix": "prettier --write ./src"
  },
```

📍 **use**

```
npm run format:check
npm run format:fix
```

📒 **.vscode/settings.json**

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

