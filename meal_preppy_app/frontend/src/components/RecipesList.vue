<template>
  <div class="container">
    <div
      class="recipes-div is-flex is-flex-direction-row
is-flex-wrap-wrap is-justify-content-space-evenly"
    >
      <div
        class="recipie-div"
        v-for="recipie of recipes"
        :key="recipie.id"
      >
        <Recipie @click="getRecipe" class="mb-6" :recipie="recipie" />
      </div>
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
          console.log(res.data);
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
.recipie-div {
  max-width: 25vw;
}
</style>
