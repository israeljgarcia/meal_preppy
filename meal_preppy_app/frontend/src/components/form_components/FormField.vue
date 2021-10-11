<template>
  <div class="container">
    <div class="field">
      <label :for="label" class="label has-text-left">{{
        labelText
      }}</label>
      <div class="control">
        <input
          class="input"
          :type="inputType"
          :name="label"
          :required="required"
          :value="modelValue"
          @input="$emit('update:modelValue', $event.target.value)"
        />
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'FormField',
  props: {
    label: String,
    labelText: String,
    inputType: String,
    required: String,
    modelValue: String,
  },

};
</script>
