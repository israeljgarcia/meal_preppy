<template>
  <div>
    <div id="nav" v-if="this.$store.state.authenticated">
      <router-link to="/home">Home</router-link> |
      <router-link to="/pantry/ingredients">Pantry</router-link> |
      <router-link to="/pantry/form">Add Ingredient</router-link> |
      <router-link to="/recipes">Recipes</router-link> |
      <router-link to="/logout">Logout</router-link>
    </div>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
