<!--
  MAIN PAGE
-->
<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Contatos telefônicos</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Novo contato</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Nome</th>
              <th scope="col">Telefone</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(contact, index) in contacts" :key="index">
              <td>{{ contact.id }}</td>
              <td>{{ contact.contact_name }}</td>
              <td>{{ contact.contact_phone }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>


<!--
  SCRIPTS THAT WILL INTERACT WITH BACKEND
-->
<script>
import axios from 'axios';
//import VueAxios from 'vue-axios'
export default {
  data() {
    return {
      contacts: [],
    };
  },
  methods: {
    /**
     * List all contacts registered in DB
    */
    listContacts() {
      const path = location.protocol + '//' + location.hostname + ':5000/';
      axios.get(path)
        .then((res) => {
          this.contacts = res.data.json_list;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.listContacts();
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
