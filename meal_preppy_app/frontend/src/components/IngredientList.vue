<template>
  <div class="container">
    <h1>Pantry List</h1>
    <hr class="heading-line" />
    <ul v-for="ingredient in ingredients" :key="ingredient.id">
      <div v-if="Object.keys(ingredients).length == 1"
        class="column is-flex is-justify-content-center is-flex-direction-column
        is-5 ingredient-container is-10-mobile"
      >
        <div
          class="is-flex ingredient-div"
          @click="getIngredientDetails"
        >
          <li class="ingredient-name">
            No Ingredients Yet! Add one?
          </li>
          <span>:)</span>
        </div>
        <hr class="item-line" />
      </div>

      <div
        class="column is-flex is-justify-content-center is-flex-direction-column
        is-5 ingredient-container is-10-mobile"
      >
        <div
          class="is-flex ingredient-div"
          @click="getIngredientDetails"
        >
          <li class="ingredient-name">
            {{ ingredient.ingredient_name }}
          </li>
          <span>{{ ingredient.quantity }} {{ ingredient.unit }}</span>
        </div>
        <hr class="item-line" />
      </div>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'IngredientList',
  data() {
    return {
      ingredients: {},
    };
  },
  methods: {
    getPantryIngredients() {
      const path = 'http://localhost:8080/pantry';
      axios
        .get(path, { headers: { Authorization: `Bearer ${localStorage.getItem('token')}` } })
        .then((res) => {
          this.ingredients = res.data;
          console.log(this.ingredients);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getPantryIngredients();
  },
};
</script>
<style scoped>
h1 {
  font-size: 2rem;
}

.heading-line {
  background: black;
  border-radius: 15px;
  height: 1.5px;
}

.item-line {
  display: block;
  background: black;
  height: 1px;
}

.ingredient-div {
  align-items: center;
  justify-content: space-between;
  margin: 0 8vw;
}

.ingredient-container {
  margin: 0 auto;
  font-size: 1.2rem;
  padding: 0;
}

.ingredient-div:hover {
  box-shadow: 0 0 10px 3px rgb(195, 195, 195);
  cursor: pointer;
  border-radius: 10px;
  padding: 0 10px;
}
</style>
