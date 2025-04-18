# 📚 Project Documentation - Algorithm Internship Test

## 🔎 1. Literature Review and Approaches
Several approaches were studied to adjust running time based on elevation:

- **Strava GAP Method**: Adjustment based on a reverse-engineered approach.
- **Daniels’ Running Formula**: Use of VDOT tables to assess effort.
- **Effort Science-Based Models**: Example, Minetti (2002) studies the energy cost of slopes.
- **Machine Learning Approaches**: Statistical models considering several parameters.

## 🛠️ 2. Method Selection
For this prototype, we selected a simple method based on a correction factor proportional to the slope grade (ascent/descent).

The applied formula is:

```python
corrected_pace = actual_pace * (1 + k * grade)

```
where k is an empirical coefficient (set here to 0.03).

This approach has the advantage of being simple to implement and easily testable with GPS data


## 3. Why This Choice?

### 🔹 Simplicity of Implementation
This method requires simple calculations (multiplication and addition) that directly transform the real pace based on a correction factor. It is easy to code and quickly validate in a testing environment.

### 🔹 Readability and Transparency
The linear relationship between ascent (or descent) and **pace** makes it easier to understand the impact of each change in elevation on performance. This allows for a clear explanation of how the algorithm works to colleagues or recruiters.

### 🔹 Adaptability to Available Data
The data extracted from a **GPX** file (latitude, longitude, altitude, and timestamp) are sufficient to apply this correction. No additional complex information is needed to implement this model.

## 4. Reasons for Rejecting Other Methods

### 4.1 Strava GAP Method
- **Complexity and Accessibility**: While the Strava GAP method is interesting, it relies on reverse engineering proprietary algorithms whose exact workings are not fully documented.
- **Unavailable Internal Data**: Strava has numerous parameters and performance histories that allow for model adjustments. In the context of a simple prototype, this information is not available, making it difficult to replicate the method accurately.

### 4.2 Daniels’ Running Formula and VDOT Tables
- **Dependence on Individual Parameters**: The Daniels formula and VDOT tables incorporate specific values related to the physiology of each runner (VO₂ max, lactate threshold, etc.).
- **Limited Adaptability to Available Data**: In our case, we only have **GPS** data from a route, without detailed individual parameters. Integrating this approach would require additional measurements and would complicate the prototype.

### 4.3 Elevation Models (e.g., Minetti 2002)
- **More Advanced Scientific Modeling**: Models like the one by Minetti are scientifically robust and integrate complex energy mechanisms to correct for the impact of elevation.
- **Complexity and Overkill for a Prototype**: Their implementation often requires precise calibration and detailed data on the physiology of effort, which goes beyond the scope of a prototype aimed mainly at demonstrating the feasibility of a correction from a GPX file.

### 4.4 Machine Learning or Advanced Physical Approach Models
- **Need for Large Data Sets**: Machine learning-based methods require a large dataset to train the model. Without such data (and within the scope of a short test), their use is not relevant.
- **Computational and Calibration Complexity**: These approaches also require a more developed modeling and validation infrastructure, which is disproportionate to the needs of a prototype aimed at illustrating a simple correction.

## 5. Prototype Description
The Python script performs the following operations:
- Reads the **GPX** file to extract GPS points (latitude, longitude, altitude, time).
- Calculates the **distance traveled** between each point using the **haversine** formula.
- Calculates the **grade** (relative elevation) for each segment.
- Calculates the **pace** (time in minutes per kilometer) for each segment.
- Applies the correction using the defined formula.

## 6. Improvement Perspectives
- 🌡️ **Integrate environmental parameters** (temperature, humidity).
- 🏃‍♂️ **Adapt the correction** based on individual characteristics (**VO₂ max**, lactate threshold, etc.).
- 🗺️ **Test and validate the algorithm** on other routes and with real data.


