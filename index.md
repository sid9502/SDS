<!DOCTYPE html>
    <html lang="en">
        

    <head>
      
      <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" />
      <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.10.0/css/bootstrap-select.min.css" rel="stylesheet" />
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tvshows</title>
     </head>
    <body style="background-color: lightgray;">

      <nav class="navbar navbar-default navbar-inverse">
        <div class="container-fluid">
          <div class="navbar-header">
            <h3 style="color:ivory; font-style:bold;">
              Movie Fetcher
            </h3>
          </div>
        </div>
      </nav>
       
        
      
        <!-- <img src="https://source.unsplash.com/collection/190727/1600x900"> -->
        <div style="width: fit-content; margin: auto; padding-block-start:20px;padding-bottom: 50px; padding-left: 80px;padding-right: 80px; border-radius: 50px; margin-top: 100px;background-image: linear-gradient(rgb(22, 207, 176),rgb(156, 218, 204)); margin-bottom: 30px; border-style: groove; border-color: black;"> 
        <form action="results" method="GET" style="width: 500px; margin:auto;">
          
            <H3 style="font-family: 'Shadows Into Light', cursive;">Enter the date </H3>
            
            <input type="date" id="tvdate" name="tvdate" style="font-family: 'Shadows Into Light', cursive;" required>

            <h3 style="font-family: 'Shadows Into Light', cursive;">Select Country <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="black" class="bi bi-geo-alt" viewBox="0 0 16 16">
              <path d="M12.166 8.94c-.524 1.062-1.234 2.12-1.96 3.07A31.493 31.493 0 0 1 8 14.58a31.481 31.481 0 0 1-2.206-2.57c-.726-.95-1.436-2.008-1.96-3.07C3.304 7.867 3 6.862 3 6a5 5 0 0 1 10 0c0 .862-.305 1.867-.834 2.94zM8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10z"/>
              <path d="M8 8a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm0 1a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
            </svg></h3>
            
            <div>
              <select  name="country" class=" form-control selectpicker" data-live-search="true" data-flip="true" required >
                <option value="">select country</option>
                <option value="AF">Afghanistan</option>
                <option value="AX">Aland Islands</option>
                <option value="AL">Albania</option>
                <option value="DZ">Algeria</option>
                <option value="AS">American Samoa</option>
                <option value="AD">Andorra</option>
                <option value="AO">Angola</option>
                <option value="AI">Anguilla</option>
                <option value="AQ">Antarctica</option>
                <option value="AG">Antigua and Barbuda</option>
                <option value="AR">Argentina</option>
                <option value="AM">Armenia</option>
                <option value="AW">Aruba</option>
                <option value="AU">Australia</option>
                <option value="AT">Austria</option>
                <option value="AZ">Azerbaijan</option>
                <option value="BS">Bahamas</option>
                <option value="BH">Bahrain</option>
                <option value="BD">Bangladesh</option>
                <option value="BB">Barbados</option>
                <option value="BY">Belarus</option>
                <option value="BE">Belgium</option>
                <option value="BZ">Belize</option>
                <option value="BJ">Benin</option>
                <option value="BM">Bermuda</option>
                <option value="BT">Bhutan</option>
                <option value="BO">Bolivia</option>
                <option value="BQ">Bonaire, Sint Eustatius and Saba</option>
                <option value="BA">Bosnia and Herzegovina</option>
                <option value="BW">Botswana</option>
                <option value="BV">Bouvet Island</option>
                <option value="BR">Brazil</option>
                <option value="IO">British Indian Ocean Territory</option>
                <option value="BN">Brunei Darussalam</option>
                <option value="BG">Bulgaria</option>
                <option value="BF">Burkina Faso</option>
                <option value="BI">Burundi</option>
                <option value="KH">Cambodia</option>
                <option value="CM">Cameroon</option>
                <option value="CA">Canada</option>
                <option value="CV">Cape Verde</option>
                <option value="KY">Cayman Islands</option>
                <option value="CF">Central African Republic</option>
                <option value="TD">Chad</option>
                <option value="CL">Chile</option>
                <option value="CN">China</option>
                <option value="CX">Christmas Island</option>
                <option value="CC">Cocos (Keeling) Islands</option>
                <option value="CO">Colombia</option>
                <option value="KM">Comoros</option>
                <option value="CG">Congo</option>
                <option value="CD">Congo, Democratic Republic of the Congo</option>
                <option value="CK">Cook Islands</option>
                <option value="CR">Costa Rica</option>
                <option value="CI">Cote D'Ivoire</option>
                <option value="HR">Croatia</option>
                <option value="CU">Cuba</option>
                <option value="CW">Curacao</option>
                <option value="CY">Cyprus</option>
                <option value="CZ">Czech Republic</option>
                <option value="DK">Denmark</option>
                <option value="DJ">Djibouti</option>
                <option value="DM">Dominica</option>
                <option value="DO">Dominican Republic</option>
                <option value="EC">Ecuador</option>
                <option value="EG">Egypt</option>
                <option value="SV">El Salvador</option>
                <option value="GQ">Equatorial Guinea</option>
                <option value="ER">Eritrea</option>
                <option value="EE">Estonia</option>
                <option value="ET">Ethiopia</option>
                <option value="FK">Falkland Islands (Malvinas)</option>
                <option value="FO">Faroe Islands</option>
                <option value="FJ">Fiji</option>
                <option value="FI">Finland</option>
                <option value="FR">France</option>
                <option value="GF">French Guiana</option>
                <option value="PF">French Polynesia</option>
                <option value="TF">French Southern Territories</option>
                <option value="GA">Gabon</option>
                <option value="GM">Gambia</option>
                <option value="GE">Georgia</option>
                <option value="DE">Germany</option>
                <option value="GH">Ghana</option>
                <option value="GI">Gibraltar</option>
                <option value="GR">Greece</option>
                <option value="GL">Greenland</option>
                <option value="GD">Grenada</option>
                <option value="GP">Guadeloupe</option>
                <option value="GU">Guam</option>
                <option value="GT">Guatemala</option>
                <option value="GG">Guernsey</option>
                <option value="GN">Guinea</option>
                <option value="GW">Guinea-Bissau</option>
                <option value="GY">Guyana</option>
                <option value="HT">Haiti</option>
                <option value="HM">Heard Island and Mcdonald Islands</option>
                <option value="VA">Holy See (Vatican City State)</option>
                <option value="HN">Honduras</option>
                <option value="HK">Hong Kong</option>
                <option value="HU">Hungary</option>
                <option value="IS">Iceland</option>
                <option value="IN">India</option>
                <option value="ID">Indonesia</option>
                <option value="IR">Iran, Islamic Republic of</option>
                <option value="IQ">Iraq</option>
                <option value="IE">Ireland</option>
                <option value="IM">Isle of Man</option>
                <option value="IL">Israel</option>
                <option value="IT">Italy</option>
                <option value="JM">Jamaica</option>
                <option value="JP">Japan</option>
                <option value="JE">Jersey</option>
                <option value="JO">Jordan</option>
                <option value="KZ">Kazakhstan</option>
                <option value="KE">Kenya</option>
                <option value="KI">Kiribati</option>
                <option value="KP">Korea, Democratic People's Republic of</option>
                <option value="KR">Korea, Republic of</option>
                <option value="XK">Kosovo</option>
                <option value="KW">Kuwait</option>
                <option value="KG">Kyrgyzstan</option>
                <option value="LA">Lao People's Democratic Republic</option>
                <option value="LV">Latvia</option>
                <option value="LB">Lebanon</option>
                <option value="LS">Lesotho</option>
                <option value="LR">Liberia</option>
                <option value="LY">Libyan Arab Jamahiriya</option>
                <option value="LI">Liechtenstein</option>
                <option value="LT">Lithuania</option>
                <option value="LU">Luxembourg</option>
                <option value="MO">Macao</option>
                <option value="MK">Macedonia, the Former Yugoslav Republic of</option>
                <option value="MG">Madagascar</option>
                <option value="MW">Malawi</option>
                <option value="MY">Malaysia</option>
                <option value="MV">Maldives</option>
                <option value="ML">Mali</option>
                <option value="MT">Malta</option>
                <option value="MH">Marshall Islands</option>
                <option value="MQ">Martinique</option>
                <option value="MR">Mauritania</option>
                <option value="MU">Mauritius</option>
                <option value="YT">Mayotte</option>
                <option value="MX">Mexico</option>
                <option value="FM">Micronesia, Federated States of</option>
                <option value="MD">Moldova, Republic of</option>
                <option value="MC">Monaco</option>
                <option value="MN">Mongolia</option>
                <option value="ME">Montenegro</option>
                <option value="MS">Montserrat</option>
                <option value="MA">Morocco</option>
                <option value="MZ">Mozambique</option>
                <option value="MM">Myanmar</option>
                <option value="NA">Namibia</option>
                <option value="NR">Nauru</option>
                <option value="NP">Nepal</option>
                <option value="NL">Netherlands</option>
                <option value="AN">Netherlands Antilles</option>
                <option value="NC">New Caledonia</option>
                <option value="NZ">New Zealand</option>
                <option value="NI">Nicaragua</option>
                <option value="NE">Niger</option>
                <option value="NG">Nigeria</option>
                <option value="NU">Niue</option>
                <option value="NF">Norfolk Island</option>
                <option value="MP">Northern Mariana Islands</option>
                <option value="NO">Norway</option>
                <option value="OM">Oman</option>
                <option value="PK">Pakistan</option>
                <option value="PW">Palau</option>
                <option value="PS">Palestinian Territory, Occupied</option>
                <option value="PA">Panama</option>
                <option value="PG">Papua New Guinea</option>
                <option value="PY">Paraguay</option>
                <option value="PE">Peru</option>
                <option value="PH">Philippines</option>
                <option value="PN">Pitcairn</option>
                <option value="PL">Poland</option>
                <option value="PT">Portugal</option>
                <option value="PR">Puerto Rico</option>
                <option value="QA">Qatar</option>
                <option value="RE">Reunion</option>
                <option value="RO">Romania</option>
                <option value="RU">Russian Federation</option>
                <option value="RW">Rwanda</option>
                <option value="BL">Saint Barthelemy</option>
                <option value="SH">Saint Helena</option>
                <option value="KN">Saint Kitts and Nevis</option>
                <option value="LC">Saint Lucia</option>
                <option value="MF">Saint Martin</option>
                <option value="PM">Saint Pierre and Miquelon</option>
                <option value="VC">Saint Vincent and the Grenadines</option>
                <option value="WS">Samoa</option>
                <option value="SM">San Marino</option>
                <option value="ST">Sao Tome and Principe</option>
                <option value="SA">Saudi Arabia</option>
                <option value="SN">Senegal</option>
                <option value="RS">Serbia</option>
                <option value="CS">Serbia and Montenegro</option>
                <option value="SC">Seychelles</option>
                <option value="SL">Sierra Leone</option>
                <option value="SG">Singapore</option>
                <option value="SX">Sint Maarten</option>
                <option value="SK">Slovakia</option>
                <option value="SI">Slovenia</option>
                <option value="SB">Solomon Islands</option>
                <option value="SO">Somalia</option>
                <option value="ZA">South Africa</option>
                <option value="GS">South Georgia and the South Sandwich Islands</option>
                <option value="SS">South Sudan</option>
                <option value="ES">Spain</option>
                <option value="LK">Sri Lanka</option>
                <option value="SD">Sudan</option>
                <option value="SR">Suriname</option>
                <option value="SJ">Svalbard and Jan Mayen</option>
                <option value="SZ">Swaziland</option>
                <option value="SE">Sweden</option>
                <option value="CH">Switzerland</option>
                <option value="SY">Syrian Arab Republic</option>
                <option value="TW">Taiwan, Province of China</option>
                <option value="TJ">Tajikistan</option>
                <option value="TZ">Tanzania, United Republic of</option>
                <option value="TH">Thailand</option>
                <option value="TL">Timor-Leste</option>
                <option value="TG">Togo</option>
                <option value="TK">Tokelau</option>
                <option value="TO">Tonga</option>
                <option value="TT">Trinidad and Tobago</option>
                <option value="TN">Tunisia</option>
                <option value="TR">Turkey</option>
                <option value="TM">Turkmenistan</option>
                <option value="TC">Turks and Caicos Islands</option>
                <option value="TV">Tuvalu</option>
                <option value="UG">Uganda</option>
                <option value="UA">Ukraine</option>
                <option value="AE">United Arab Emirates</option>
                <option value="GB">United Kingdom</option>
                <option value="US">United States</option>
                <option value="UM">United States Minor Outlying Islands</option>
                <option value="UY">Uruguay</option>
                <option value="UZ">Uzbekistan</option>
                <option value="VU">Vanuatu</option>
                <option value="VE">Venezuela</option>
                <option value="VN">Viet Nam</option> -->
                 <option value="VG">Virgin Islands, British</option>
                <option value="VI">Virgin Islands, U.s.</option>
                <option value="WF">Wallis and Futuna</option>
                <option value="EH">Western Sahara</option>
                <option value="YE">Yemen</option>
                <option value="ZM">Zambia</option>
                <option value="ZW">Zimbabwe</option>
            </select> 
          </div>
          <div style="padding-top: 25px; padding-bottom: 20px;">
          <h3 style="font-family: 'Shadows Into Light', cursive;padding-bottom: 20px; padding-top: 20px;">Filters: <span class="glyphicon glyphicon-filter" aria-hidden="true"></span></h3>
          
        
          <h4 style="font-family: 'Shadows Into Light', cursive;">Show Rating</h4>
 
          <select  name="show_rating" class="form-control selectpicker" data-live-search="true" >
    
              <option value="0">-----</option>
              <option value="2">2+</option>
              <option value="3">3+</option>
              <option value="4">4+</option>
              <option value="5">5+</option>
              <option value="6">6+</option>
              <option value="7">7+</option>
              <option value="8">8+</option>
              <option value="9">9+</option>
              </select>
              <br>
            </div>
          <div style="padding-top: 30px;">
          <h4 style="font-family: 'Shadows Into Light', cursive; ">Language </h4> 
          </div>
          <div>  
          <select  name="Language" class="form-control selectpicker" data-live-search="true" autofocus="false">

                <option value="0">-----</option>
                <option value="Afrikaans">Afrikaans</option>
                <option value="Albanian">Albanian</option>
                <option value="Arabic">Arabic</option>
                <option value="Armenian">Armenian</option>
                <option value="Azerbaijani">Azerbaijani</option>
                <option value="Basque">Basque</option>
                <option value="Belarusian">Belarusian</option>
                <option value="Bengali">Bengali</option>
                <option value="Bosnian">Bosnian</option>
                <option value="Bulgarian">Bulgarian</option>
                <option value="Catalan">Catalan</option>
                <option value="Chechen">Chechen</option>
                <option value="Chinese">Chinese</option>
                <option value="Croatian">Croatian</option>
                <option value="Czech">Czech</option>
                <option value="Danish">Danish</option>
                <option value="Divehi">Divehi</option>
                <option value="Dutch">Dutch</option>
                <option value="English">English</option>
                <option value="Estonian">Estonian</option>
                <option value="Finnish">Finnish</option>
                <option value="French">French</option>
                <option value="Galician">Galician</option>
                <option value="Georgian">Georgian</option>
                <option value="German">German</option>
                <option value="Greek">Greek</option>
                <option value="Gujarati">Gujarati</option>
                <option value="Hebrew">Hebrew</option>
                <option value="Hindi">Hindi</option>
                <option value="Hungarian">Hungarian</option>
                <option value="Icelandic">Icelandic</option>
                <option value="Indonesian">Indonesian</option>
                <option value="Irish">Irish</option>
                <option value="Italian">Italian</option>
                <option value="Japanese">Japanese</option>
                <option value="Javanese">Javanese</option>
                <option value="Kannada">Kannada</option>
                <option value="Kazakh">Kazakh</option>
                <option value="Kongo">Kongo</option>
                <option value="Korean">Korean</option>
                <option value="Latin">Latin</option>
                <option value="Latvian">Latvian</option>
                <option value="Lithuanian">Lithuanian</option>
                <option value="Luxembourgish">Luxembourgish</option>
                <option value="Malay">Malay</option>
                <option value="Malayalam">Malayalam</option>
                <option value="Marathi">Marathi</option>
                <option value="Mongolian">Mongolian</option>
                <option value="Norwegian">Norwegian</option>
                <option value="Panjabi">Panjabi</option>
                <option value="Pashto">Pashto</option>
                <option value="Persian">Persian</option>
                <option value="Polish">Polish</option>
                <option value="Portuguese">Portuguese</option>
                <option value="Romanian">Romanian</option>
                <option value="Russian">Russian</option>
                <option value="Serbian">Serbian</option>
                <option value="Sinhalese">Sinhalese</option>
                <option value="Slovak">Slovak</option>
                <option value="Slovenian">Slovenian</option>
                <option value="Spanish">Spanish</option>
                <option value="Swedish">Swedish</option>
                <option value="Tagalog">Tagalog</option>
                <option value="Tamil">Tamil</option>
                <option value="Telugu">Telugu</option>
                <option value="Thai">Thai</option>
                <option value="Turkish">Turkish</option>
                <option value="Ukrainian">Ukrainian</option>
                <option value="Urdu">Urdu</option>
                <option value="Uzbek">Uzbek</option>
                <option value="Vietnamese">Vietnamese</option>
                <option value="Welsh">Welsh</option>
                <option value="Scottish Gaelic">Scottish Gaelic</option>
                </select>
              </div>
            <br>
            <div style="padding-top: 30px;">
            <H3 style="font-family: 'Shadows Into Light', cursive;">Genre</H3>
          </div>
            <select  name="Genre" class="form-control selectpicker" data-live-search="true" data-flip="true" >
              <option value="0">-----</option>
              <option value="Action">Action</option>
              <option value="Adult">Adult</option>
              <option value="Adventure">Adventure</option>
              <option value="Anime">Anime</option>
              <option value="Children">Children</option>
              <option value="Comedy">Comedy</option>
              <option value="Crime">Crime</option>
              <option value="DIY">DIY</option>
              <option value="Drama">Drama</option>
              <option value="Espionage">Espionage</option>
              <option value="Family">Family</option>
              <option value="Fantasy">Fantasy</option>
              <option value="Food">Food</option>
              <option value="History">History</option>
              <option value="Horror">Horror</option>
              <option value="Legal">Legal</option>
              <option value="Medical">Medical</option>
              <option value="Music">Music</option>
              <option value="Mystery">Mystery</option>
              <option value="Nature">Nature</option>
              <option value="Romance">Romance</option>
              <option value="Science-Fiction">Science-Fiction</option>
              <option value="Sports">Sports</option>
              <option value="Supernatural">Supernatural</option>
              <option value="Thriller">Thriller</option>
              <option value="Travel">Travel</option>
              <option value="War">War</option>
              <option value="Western">Western</option>
            </select>
              
              
              <div style="padding-top: 60px; padding-left: 85px;">
               <span ><button type="submit" class="btn btn-secondary " style="display: inline-block; width: 100px ;height: 40px">Submit</button> </span> 
              <span> 
                <select  aria-label="Default select example" data-toggle="Dropdown" style="display: inline-block; width: 200px; height: 40px; border-radius: 5px; margin-left: 35px; margin-top: 20px;" name="Sort">
                  <option selected>Sort By</option>
                  <option value="0">A to Z</option>
                  <option value="1">Z to A</option>
                  <!-- <option value="2">Rating</option> -->
                </select>
              </span> 
            </div>

          </div>
            
          
            
            </div>
              
              
                
              
            
            
          </form>
        </div>
          
          
          
          
            <!-- <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false" name="Sort">
                  Dropdown button
                </button> -->
                <!-- <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1" >
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul> -->
              <!-- </div> -->
              
           
            
              
     <!-- <a href="results">Link to the next page</a> -->
     <!-- <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script> -->
     
     <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
     <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.10.0/js/bootstrap-select.min.js"></script>
    </body>
    </html>
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
