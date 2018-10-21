% rebase("layout.tpl", title="Store App - Add")
% if "permissions" in sess and sess["permissions"] == "MANAGER":
<div class="container">
  <div class="row">
    <div class="twelve column" style="margin-top: 10%">
      <h4 style="text-align: center">Add New Product</h4>
    </div>
  </div>
  <form action="/add/product" method="POST">
    <fieldset>
      <div class="row", style="margin-top: 5%">
        <div class="six columns">
          <label for="name">Product Name</label>
          <input class="u-full-width" id="name" type="text" placeholder="apple" name="name">
        </div>
        <div class="three columns">
          <label for="quantity">Quantity</label>
          <input class="u-full-width" id="quantity" type="number" placeholder="3" name="quantity">
        </div>
        <div class="three columns">
          <label for="price">Price (without '$')</label>
          <input class="u-full-width" id="price" type="text" placeholder="1.50" name="price">
        </div>
      </div>
      <div class="row", style="margin-top: 5%">
        <div class="six columns">
          <label for="provider">Provider</label>
          <input class="u-full-width" id="provider" type="text" placeholder="Fruits, inc." name="provider">
        </div>
        <div class="six columns">
          <label for="provider_contact">Provider Telephone Number</label>
          <input class="u-full-width" id="provider_contact" type="tel" placeholder="555-555-5555" name="provider_contact">
        </div>
      </div>
      <a class="button" href="/", style="margin: 3%; margin-left: 0%">Cancel</a>
      <input class="button-primary" type="submit" value="Submit">

    </fieldset>
  </form>
</div>
% else:
 % include('denied.tpl')