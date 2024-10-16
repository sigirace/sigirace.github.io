📍 **Babel plugin dependencies**

```
One of your dependencies, babel-preset-react-app, is importing the
"@babel/plugin-proposal-private-property-in-object" package without
declaring it in its dependencies. This is currently working because
"@babel/plugin-proposal-private-property-in-object" is already in your
node_modules folder for unrelated reasons, but it may break at any time.

babel-preset-react-app is part of the create-react-app project, which
is not maintianed anymore. It is thus unlikely that this bug will
ever be fixed. Add "@babel/plugin-proposal-private-property-in-object" to
your devDependencies to work around this error. This will make this message
go away.
```

이 메시지는 babel-preset-react-app 패키지가 @babel/plugin-proposal-private-property-in-object 패키지를 의존성으로 선언하지 않고 사용하고 있다는 경고입니다. 이 문제는 현재 node_modules 폴더에 이미 존재하기 때문에 작동하고 있지만, 향후에 문제가 발생할 수 있습니다.

이 문제를 해결하기 위해 @babel/plugin-proposal-private-property-in-object를 devDependencies에 추가해야 합니다. 아래는 이를 추가하는 방법입니다.

```
npm install --save-dev @babel/plugin-proposal-private-property-in-object
```

