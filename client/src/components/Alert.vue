<!--
    This template will be added here to show how other componets may integrate page
-->
<template>
  <div>
    <b-alert show>{{ message }}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message'],
};
</script>