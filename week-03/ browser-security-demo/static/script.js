// ==========================================
// SECURE SERVER-SIDE DEMO
// ==========================================


// Get the button from the page

const secureButton =
    document.getElementById("secure-button");


// This is where we will display
// the server response

const secureResult =
    document.getElementById("secure-result");



// ==========================================
// WHEN USER CLICKS THE BUTTON
// ==========================================

secureButton.addEventListener(
    "click",

    async () => {


        // Show temporary message

        secureResult.innerHTML =
            "Checking authorization with the server...";



        try {


            // ==================================
            // REQUEST PRO DATA FROM SERVER
            // ==================================

            const response =
                await fetch("/api/pro-data");


            const data =
                await response.json();



            // ==================================
            // SERVER DENIED ACCESS
            // ==================================

            if (response.status === 403) {


                secureResult.innerHTML = `

                    <div class="access-denied">

                        <strong>
                            ❌ 403 FORBIDDEN
                        </strong>


                        <p>
                            Access denied by the server.
                        </p>


                        <p>
                            ${data.message}
                        </p>


                    </div>

                `;


                return;

            }



            // ==================================
            // SERVER APPROVED ACCESS
            // ==================================

            if (response.ok) {


                secureResult.innerHTML = `

                    <div class="access-granted">

                        <strong>
                            ✅ ACCESS GRANTED
                        </strong>


                        <h3>
                            ${data.feature}
                        </h3>


                        <p>
                            Monthly Revenue:
                            ${data.monthly_revenue}
                        </p>


                        <p>
                            Growth Rate:
                            ${data.growth_rate}
                        </p>


                    </div>

                `;

            }


        }


        // ======================================
        // SERVER CONNECTION ERROR
        // ======================================

        catch (error) {


            secureResult.innerHTML = `

                <div class="access-denied">

                    <strong>
                        Server connection failed.
                    </strong>

                </div>

            `;


            console.error(error);

        }


    }

);