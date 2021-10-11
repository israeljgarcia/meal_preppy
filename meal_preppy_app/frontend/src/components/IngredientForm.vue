<template>
  <div class="container">
    <div class="columns is-centered">
      <form class="card column is-10-mobile is-4 py-6" method="POST">
        <h1 class="pb-6 is-size-4 has-text-weight-bold">
          Add Ingredient
        </h1>
        <FormField
          class="column is-10"
          label="ingredientName"
          labelText="Ingredient Name"
          inputType="text"
          required="required"
          v-model="ingredientName"
        />

        <FormField
          class="column is-10"
          label="quantity"
          labelText="Quantity"
          inputType="number"
          required="required"
          v-model="quantity"
        />

        <FormField
          class="column is-10"
          label="unit"
          labelText="Units"
          inputType="text"
          required="required"
          v-model="unit"
        />

        <Button @click="addIngredient" buttonTxt="Add Ingredient" />
      </form>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import FormField from './form_components/FormField.vue';
import Button from './form_components/Button.vue';

export default {
  name: 'IngredientForm',
  components: {
    FormField,
    Button,
  },
  data() {
    return {
      ingredientName: '',
      quantity: '',
      unit: '',
    };
  },
  methods: {
    addIngredient(e) {
      const path = 'http://localhost:5000/pantry/addingredient';

      e.preventDefault();

      axios
        .post(
          path,
          {
            ingredientName: this.ingredientName,
            quantity: this.quantity,
            unit: this.unit,
          },
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem(
                'token',
              )}`,
            },
          },
        )
        .then((res) => {
          if (res.data.message !== 'error') {
            this.$router.push({ name: 'Pantry' });
          } else {
            console.log(res);
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
