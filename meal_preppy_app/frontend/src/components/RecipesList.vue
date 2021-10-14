<template>
  <div class="container columns is-centered is-multiline">
    <div
      class="column is-4"
      v-for="recipie of recipes"
      :key="recipie.id"
    >
      <Recipie @click="getRecipe" :recipie="recipie" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Recipie from './Recipie.vue';

export default {
  name: 'RecipesList',
  components: {
    Recipie,
  },
  data() {
    return {
      recipes: {},
    };
  },
  methods: {
    getRecipes() {
      const path = 'http://localhost:5000/api/recipes';

      axios
        .get(path, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`,
          },
        })
        .then((res) => {
          this.recipes = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getRecipes();
  },
};
</script>
<style scoped>
  .container {
    margin: 0 auto;
  }
</style>
