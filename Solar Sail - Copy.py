#imports
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.optimize import curve_fit

#constants
G = 6.67e-11
Year_Seconds = 31536000
time_running = 0.5              # How many years will the program run
# Solar Probe

# This is a 2d dimensional attempt to simulate a sun fly-by-ing probe with a solar sail
# The probe will attempt to exit the system along the axis of the sun

# The Sun
The_Sun_Mass = 1.998e30  # Kilograms
The_Sun_Radius = 695.7e6 # Metres    Everything (unless specified) will be in SI units
# Variables; for the sun, these will remain constant
The_Sun_Position = [0,0] # The sun will be located at our centre of frame ## We will forget Jupiter and its gravitational influence exists for now 
The_Sun_Velocity = [0,0]
The_Sun_Acceleration = [0,0]
# SUN
The_Sun =[The_Sun_Position,     # 0: Position 1: Velocity 2: Acceleration 3: Mass 4: Radius
          The_Sun_Velocity,
          The_Sun_Acceleration,
          The_Sun_Mass,
          The_Sun_Radius]

# The Earth
Eath_Mass = 5.97e24 # Kilo
Eath_Rad_Equatorial = 6378e3 # Metres 
# Variables
Earth_Position = np.array([0.0, 0.0])
Earth_Velocity = np.array([0.0, 0.0])
Earth_Acceleration = np.array([0.0, 0.0])
# EARTH
The_Earth = [Earth_Position,
             Earth_Velocity,
             Earth_Acceleration,
             Eath_Mass,
             Eath_Rad_Equatorial]

# The Probe (Nicknamed: Civilian 1) 
# The Probe (Civilian 1)
GramsPerMetreSquared = 0.1
Civ1_SailArea = 100000           # m^2
Civ1_TotalMass = ( (Civ1_SailArea*GramsPerMetreSquared)/1000 )  +  50        # kg
Civ1_Reflective_Index = 0.90

Civ1_Position = np.array([149e9, 0.0])
Civ1_Velocity = np.array([0.0, 20000.0])##########################################
Civ1_Acceleration = np.array([0.0, 0.0])

The_Probe = [
    Civ1_Position,
    Civ1_Velocity,
    Civ1_Acceleration,
    Civ1_TotalMass,
    Civ1_SailArea
]

Front_Panel=1 #1m^2
Side_Panels=2 #2m^2
Back_Panel=1
Front_Panel_Emissivity=0.67 # Source: Damook et. al., 2019 
Other_Sides_Emissivity=0.67
Front_Panel_Absorption=0.25
Other_Sides_Absorption=0.25

The_Probe_Surfaces = [
    Front_Panel,
    Side_Panels,
    Back_Panel,
    Front_Panel_Emissivity,
    Other_Sides_Emissivity,
    Front_Panel_Absorption,
    Other_Sides_Absorption
]

Front_Reflector   = Civ1_SailArea
Back_of_Reflector = Civ1_SailArea
Front_Reflector_Emissivity   = 0.73
Back_of_Reflector_Emissivity = 0.73
Front_Reflector_Absorption   = 0.15
Back_of_Reflector_Absorption = 0.15

The_Sail_Surfaces = [ # Aluminised Mylar
    Front_Reflector,
    Back_of_Reflector,
    Front_Reflector_Emissivity,
    Back_of_Reflector_Emissivity,
    Front_Reflector_Absorption,
    Back_of_Reflector_Absorption
]

# =====================================  OTHER PLANETS

# ============================================================
# MERCURY
# ============================================================

Mercury_Mass = 3.3011e23                 # kg
Mercury_Rad_Equatorial = 2439.7e3       # metres

Mercury_Position = np.array([0.0, 0.0])
Mercury_Velocity = np.array([0.0, 0.0])
Mercury_Acceleration = np.array([0.0, 0.0])

The_Mercury = [
    Mercury_Position,
    Mercury_Velocity,
    Mercury_Acceleration,
    Mercury_Mass,
    Mercury_Rad_Equatorial
]


# ============================================================
# VENUS
# ============================================================

Venus_Mass = 4.8675e24                  # kg
Venus_Rad_Equatorial = 6051.8e3         # metres

Venus_Position = np.array([0.0, 0.0])
Venus_Velocity = np.array([0.0, 0.0])
Venus_Acceleration = np.array([0.0, 0.0])

The_Venus = [
    Venus_Position,
    Venus_Velocity,
    Venus_Acceleration,
    Venus_Mass,
    Venus_Rad_Equatorial
]



# ============================================================
# MARS
# ============================================================

Mars_Mass = 6.4171e23                   # kg
Mars_Rad_Equatorial = 3396.2e3          # metres

Mars_Position = np.array([0.0, 0.0])
Mars_Velocity = np.array([0.0, 0.0])
Mars_Acceleration = np.array([0.0, 0.0])

The_Mars = [
    Mars_Position,
    Mars_Velocity,
    Mars_Acceleration,
    Mars_Mass,
    Mars_Rad_Equatorial
]


# ============================================================
# JUPITER
# ============================================================

Jupiter_Mass = 1.8982e27                # kg
Jupiter_Rad_Equatorial = 71492.0e3      # metres

Jupiter_Position = np.array([0.0, 0.0])
Jupiter_Velocity = np.array([0.0, 0.0])
Jupiter_Acceleration = np.array([0.0, 0.0])

The_Jupiter = [
    Jupiter_Position,
    Jupiter_Velocity,
    Jupiter_Acceleration,
    Jupiter_Mass,
    Jupiter_Rad_Equatorial
]


# ============================================================
# SATURN
# ============================================================

Saturn_Mass = 5.6834e26                 # kg
Saturn_Rad_Equatorial = 60268.0e3       # metres

Saturn_Position = np.array([0.0, 0.0])
Saturn_Velocity = np.array([0.0, 0.0])
Saturn_Acceleration = np.array([0.0, 0.0])

The_Saturn = [
    Saturn_Position,
    Saturn_Velocity,
    Saturn_Acceleration,
    Saturn_Mass,
    Saturn_Rad_Equatorial
]


# ============================================================
# URANUS
# ============================================================

Uranus_Mass = 8.6810e25                  # kg
Uranus_Rad_Equatorial = 25559.0e3        # metres

Uranus_Position = np.array([0.0, 0.0])
Uranus_Velocity = np.array([0.0, 0.0])
Uranus_Acceleration = np.array([0.0, 0.0])

The_Uranus = [
    Uranus_Position,
    Uranus_Velocity,
    Uranus_Acceleration,
    Uranus_Mass,
    Uranus_Rad_Equatorial
]


# ============================================================
# NEPTUNE
# ============================================================

Neptune_Mass = 1.02413e26                # kg
Neptune_Rad_Equatorial = 24764.0e3       # metres

Neptune_Position = np.array([0.0, 0.0])
Neptune_Velocity = np.array([0.0, 0.0])
Neptune_Acceleration = np.array([0.0, 0.0])

The_Neptune = [
    Neptune_Position,
    Neptune_Velocity,
    Neptune_Acceleration,
    Neptune_Mass,
    Neptune_Rad_Equatorial
]





def Temperature_of_Probe(Probe, angle):
    L = 3.828e26
    x, y = Probe[0]

    r = np.array([x, y])
    distance = np.linalg.norm(r)

    Stefan_Boltzmann = 5.67037e-8
    Solar_Rads = L / (4*np.pi*distance**2)

    In_Surface = (The_Probe_Surfaces[0]*The_Probe_Surfaces[5]*np.cos(angle) +   # Front panel
                    The_Probe_Surfaces[1]*The_Probe_Surfaces[6]*np.sin(angle))  # Side Panel that is slightly exposed
    
    Out_Surface = (The_Probe_Surfaces[0]*The_Probe_Surfaces[3] +
                   The_Probe_Surfaces[1]*The_Probe_Surfaces[4] +
                   The_Probe_Surfaces[2]*The_Probe_Surfaces[4])
    
    Sail_In_Surface = (The_Sail_Surfaces[0]*The_Sail_Surfaces[4]*np.cos(angle))

    Sail_Out_Surface = (The_Sail_Surfaces[0]*The_Sail_Surfaces[2] +
                        The_Sail_Surfaces[1]*The_Sail_Surfaces[3])

    Temp = np.sqrt(np.sqrt( (In_Surface*Solar_Rads) / (Out_Surface*Stefan_Boltzmann) ))
    Temp_Sail = np.sqrt(np.sqrt( (Sail_In_Surface*Solar_Rads) / (Sail_Out_Surface*Stefan_Boltzmann) ))
    return Temp, Temp_Sail

Escape_Velocity = 0
sideways_velocity_array = []

def SteeringNormal(probe,Tic):
    global Escape_Velocity
    r = probe[0]
    v = probe[1]

    r_hat = r / np.linalg.norm(r)
    v_hat = v / np.linalg.norm(v)

    tangent = np.array([-r_hat[1], r_hat[0]])

    radial = np.dot(v_hat, r_hat)
    sideways = np.dot(v_hat, tangent)
    sideways_velocity = np.dot(v, tangent)
    radial_velocity = np.dot(v, r_hat)
    gain = 1 ######################################################

    if sideways_velocity >= 20:
        desired = r_hat - gain * tangent  # * sideways  #<--- More Variable, the steepness of the angle is dependent on the velocity vector 
    if sideways_velocity <= 20:
        desired = r_hat - gain * tangent  * sideways  #<--- More Variable, the steepness of the angle is dependent on the velocity vector 

    desired /= np.linalg.norm(desired)

    distance = np.linalg.norm(r)
    if Tic >= Year_Seconds*(2/3)/100:
        sideways_velocity_array.append(sideways_velocity)

            #print(sideways_velocity)
            #print(radial_velocity-np.sqrt(2*G*The_Sun_Mass/distance))
    Escape_Velocity = radial_velocity-np.sqrt(2*G*The_Sun_Mass/distance)
    return desired

# Solar radiation pressure acceleration
def Solar_Sail_Force(Sun, Probe,Tic):

    

    L = 3.828e26
    c = 299792458

    x, y = Probe[0]

    r = np.array([x, y])
    distance = np.linalg.norm(r)

    if distance == 0:
        return np.zeros(2)

    r_hat = r / distance

    # Rotate 90° anticlockwise
    t_hat = np.array([-r_hat[1], r_hat[0]])
    distance = np.linalg.norm(Probe[0])
 
    # Sail normal
    Close_Switch = 2#####################################################
    
    
    if Probe[0][1] >= -1:
        cosTheta = 0
        normal = r_hat
    if Probe[0][1] <= -1:
        if distance < Close_Switch*149e9:
            normal = r_hat
            cosTheta = 1.0
        if distance > Close_Switch*149e9:
            normal = SteeringNormal(Probe,Tic)
            cosTheta = np.dot(r_hat, normal)
        

    pressure = L / (4*np.pi*distance**2*c)

    

    force = (
        pressure
        * Probe[4]                     # area
        * (1.0 + Civ1_Reflective_Index)
        * cosTheta**2
    )


    acceleration = force * normal / Probe[3]

    return acceleration, cosTheta
def Suns_Gravity(Mass_A, Mass_B):
    # Position of Body B relative to the Sun
    x = Mass_B[0][0]
    y = Mass_B[0][1]

    # Distance from the Sun
    Distance = np.sqrt(x**2 + y**2)

    if Distance == 0:
        return np.array([0.0, 0.0])

    # Magnitude of acceleration
    Accel_Scalar = G * Mass_A[3] / Distance**2

    # Acceleration always points towards the Sun
    x_accel = -Accel_Scalar * x / Distance
    y_accel = -Accel_Scalar * y / Distance

    return np.array([x_accel, y_accel])

def Planet_Gravity(Planet, Sat_Civ):
    # Position of Body B relative to the Planet
    Mass_Planet = Planet[3]
    
    xPlanet=Planet[0][0]
    yPlanet=Planet[0][1]
    xSat=Sat_Civ[0][0]
    ySat=Sat_Civ[0][1]

    xDistance = xPlanet-xSat
    yDistance = yPlanet-ySat
    # Distance from the Planet
    Distance = np.sqrt(xDistance**2 + yDistance**2)

    if Distance == 0:
        return np.array([0.0, 0.0]), 0.0

    # Magnitude of acceleration
    Accel_Scalar = G * Mass_Planet / Distance**2

    # Acceleration always points towards the Planet
    x_accel = Accel_Scalar * xDistance / Distance
    y_accel = Accel_Scalar * yDistance / Distance

    return np.array([x_accel, y_accel]), Distance
        
                    
savedmercurydata = []
savedvenusdata = []
savedearthdata = []
savedmarsdata = []
savedjupiterdata = []
savedsaturndata = []
saveduranusdata = []
savedneptunedata = []

savedprobeData = []
savedFlightAngle=[]
savedSpeed=[]
savedTempData=[]
savedTempSailData=[]
savedProbeMercuryDistance=[]

Angle_At_Mercury_Flyby_probes = 0
Angle_At_Mercury_Flyby_mercurys = 0

VitalTempPoints = [0, 0, 0, 0, 0,0]
VitalTempSailPoints = [0, 0, 0, 0, 0,0]
VitalAngles = [0, 0, 0, 0, 0,0]
VitalPositions  = [None, None, None, None, None, None]
VitalTickPoints = [None, None, None, None, None, None]
VitalVelocity   = [None, None, None, None, None, None]
def Run_Time(TimePass, TickSpeed):
    global Angle_At_Mercury_Flyby_mercurys, Angle_At_Mercury_Flyby_probes
    Temp1 = 0
    Temp2 = 0
    Temp3 = 0
    Ticks = round(TimePass / TickSpeed)

    for tic in range(Ticks):

        # EARTH gravity ============================================
        The_Earth[2] = Suns_Gravity(The_Sun, The_Earth)

        The_Earth[0] += (
            The_Earth[1] * TickSpeed
            + 0.5 * The_Earth[2] * TickSpeed**2
        )

        NewEarthAccel = Suns_Gravity(The_Sun, The_Earth)

        The_Earth[1] += (
            0.5 *
            (The_Earth[2] + NewEarthAccel)
            * TickSpeed
        )

        The_Earth[2] = NewEarthAccel
        # ============================================================
        # MERCURY GRAVITY
        # ============================================================

        The_Mercury[2] = Suns_Gravity(The_Sun, The_Mercury)

        The_Mercury[0] += (
            The_Mercury[1] * TickSpeed
            + 0.5 * The_Mercury[2] * TickSpeed**2
        )

        NewMercuryAccel = Suns_Gravity(The_Sun, The_Mercury)

        The_Mercury[1] += (
            0.5
            * (The_Mercury[2] + NewMercuryAccel)
            * TickSpeed
        )

        The_Mercury[2] = NewMercuryAccel


        # ============================================================
        # VENUS GRAVITY
        # ============================================================

        The_Venus[2] = Suns_Gravity(The_Sun, The_Venus)

        The_Venus[0] += (
            The_Venus[1] * TickSpeed
            + 0.5 * The_Venus[2] * TickSpeed**2
        )

        NewVenusAccel = Suns_Gravity(The_Sun, The_Venus)

        The_Venus[1] += (
            0.5
            * (The_Venus[2] + NewVenusAccel)
            * TickSpeed
        )

        The_Venus[2] = NewVenusAccel


        # ============================================================
        # MARS GRAVITY
        # ============================================================

        The_Mars[2] = Suns_Gravity(The_Sun, The_Mars)

        The_Mars[0] += (
            The_Mars[1] * TickSpeed
            + 0.5 * The_Mars[2] * TickSpeed**2
        )

        NewMarsAccel = Suns_Gravity(The_Sun, The_Mars)

        The_Mars[1] += (
            0.5
            * (The_Mars[2] + NewMarsAccel)
            * TickSpeed
        )

        The_Mars[2] = NewMarsAccel


        # ============================================================
        # JUPITER GRAVITY
        # ============================================================

        The_Jupiter[2] = Suns_Gravity(The_Sun, The_Jupiter)

        The_Jupiter[0] += (
            The_Jupiter[1] * TickSpeed
            + 0.5 * The_Jupiter[2] * TickSpeed**2
        )

        NewJupiterAccel = Suns_Gravity(The_Sun, The_Jupiter)

        The_Jupiter[1] += (
            0.5
            * (The_Jupiter[2] + NewJupiterAccel)
            * TickSpeed
        )

        The_Jupiter[2] = NewJupiterAccel


        # ============================================================
        # SATURN GRAVITY
        # ============================================================

        The_Saturn[2] = Suns_Gravity(The_Sun, The_Saturn)

        The_Saturn[0] += (
            The_Saturn[1] * TickSpeed
            + 0.5 * The_Saturn[2] * TickSpeed**2
        )

        NewSaturnAccel = Suns_Gravity(The_Sun, The_Saturn)

        The_Saturn[1] += (
            0.5
            * (The_Saturn[2] + NewSaturnAccel)
            * TickSpeed
        )

        The_Saturn[2] = NewSaturnAccel


        # ============================================================
        # URANUS GRAVITY
        # ============================================================

        The_Uranus[2] = Suns_Gravity(The_Sun, The_Uranus)

        The_Uranus[0] += (
            The_Uranus[1] * TickSpeed
            + 0.5 * The_Uranus[2] * TickSpeed**2
        )

        NewUranusAccel = Suns_Gravity(The_Sun, The_Uranus)

        The_Uranus[1] += (
            0.5
            * (The_Uranus[2] + NewUranusAccel)
            * TickSpeed
        )

        The_Uranus[2] = NewUranusAccel


        # ============================================================
        # NEPTUNE GRAVITY
        # ============================================================

        The_Neptune[2] = Suns_Gravity(The_Sun, The_Neptune)

        The_Neptune[0] += (
            The_Neptune[1] * TickSpeed
            + 0.5 * The_Neptune[2] * TickSpeed**2
        )

        NewNeptuneAccel = Suns_Gravity(The_Sun, The_Neptune)

        The_Neptune[1] += (
            0.5
            * (The_Neptune[2] + NewNeptuneAccel)
            * TickSpeed
        )

        The_Neptune[2] = NewNeptuneAccel


        # PROBE gravity + sail
        GravityAccel = Suns_Gravity(The_Sun, The_Probe) + Planet_Gravity(The_Mercury, The_Probe)[0]
        SailAccel, SailCosTheta = Solar_Sail_Force(The_Sun, The_Probe, tic)
    
        SailAngle = np.acos(SailCosTheta)
        The_Probe[2] = GravityAccel + SailAccel


        The_Probe[0] += (
            The_Probe[1] * TickSpeed
            + 0.5 * The_Probe[2] * TickSpeed**2
        )

        NewProbeAccel = (
            Suns_Gravity(The_Sun, The_Probe) + Planet_Gravity(The_Mercury, The_Probe)[0]
            + Solar_Sail_Force(The_Sun, The_Probe,tic)[0]
        )


        The_Probe[1] += (
            0.5 *
            (The_Probe[2] + NewProbeAccel)
            * TickSpeed
        )

        Probe_Distance_To_Mercury = Planet_Gravity(The_Mercury, The_Probe)[1]

        The_Probe[2] = NewProbeAccel
        r = The_Probe[0]
        v = The_Probe[1]

        r_hat = r / np.linalg.norm(r)

        radial_speed = np.dot(v, r_hat)

        tangent = np.array([-r_hat[1], r_hat[0]])

        tangential_speed = np.dot(v, tangent)

        flight_angle = np.degrees(
            np.arctan2(
            tangential_speed,
            radial_speed
            )
        )
        probe_Distance = np.linalg.norm(r)
        probe_speed = np.linalg.norm(v)
        Temp, Temp_Sail = Temperature_of_Probe(The_Probe, SailAngle)

        angle = np.degrees(np.arctan2(r[1], r[0])) % 360

        if 1 <= angle <= 2 and VitalTickPoints[0] is None:
            VitalTempPoints[0] = Temp
            VitalTempSailPoints[0] = Temp_Sail
            VitalPositions[0] = The_Probe[0].copy()
            VitalTickPoints[0] = tic
            VitalVelocity[0] = probe_speed
            VitalAngles[0] = SailAngle
        if 45 <= angle <= 46 and VitalTickPoints[1] is None:
            VitalTempPoints[1] = Temp
            VitalTempSailPoints[1] = Temp_Sail
            VitalPositions[1] = The_Probe[0].copy()
            VitalTickPoints[1] = tic
            VitalVelocity[1] = probe_speed
            VitalAngles[1] = SailAngle
        if 90 <= angle <= 91 and VitalTickPoints[2] is None:
            VitalTempPoints[2] = Temp
            VitalTempSailPoints[2] = Temp_Sail
            VitalPositions[2] = The_Probe[0].copy()
            VitalTickPoints[2] = tic
            VitalVelocity[2] = probe_speed
            VitalAngles[2] = SailAngle
        if 180.5 <= angle <= 181 and VitalTickPoints[3] is None:
            VitalTempPoints[3] = Temp
            VitalTempSailPoints[3] = Temp_Sail
            VitalPositions[3] = The_Probe[0].copy()
            VitalTickPoints[3] = tic
            VitalVelocity[3] = probe_speed
            VitalAngles[3] = SailAngle
        if 225 <= angle <= 226 and VitalTickPoints[4] is None:
            VitalTempPoints[4] = Temp
            VitalTempSailPoints[4] = Temp_Sail
            VitalPositions[4] = The_Probe[0].copy()
            VitalTickPoints[4] = tic
            VitalVelocity[4] = probe_speed
            VitalAngles[4] = SailAngle
        if 1.5*149e9 <= probe_Distance <= 3*149e9 and VitalTickPoints[5] is None:
            VitalTempPoints[5] = Temp
            VitalTempSailPoints[5] = Temp_Sail
            VitalPositions[5] = The_Probe[0].copy()
            VitalTickPoints[5] = tic
            VitalVelocity[5] = probe_speed
            VitalAngles[5] = SailAngle
        if probe_Distance <= 57.91e9:         #Mercury point
            Probe_Distance_To_Mercury_Along_Orbit = Planet_Gravity(The_Mercury, The_Probe)[1]
            Angle_At_Mercury_Flyby_probes = np.degrees(
            np.arctan2(The_Probe[0][1], The_Probe[0][0])
            ) % 360
            Angle_At_Mercury_Flyby_mercurys = np.degrees(
            np.arctan2(The_Mercury[0][1], The_Mercury[0][0])
            ) % 360
        savedProbeMercuryDistance.append(Probe_Distance_To_Mercury.copy())
        savedTempData.append(Temp.copy())
        savedTempSailData.append(Temp_Sail.copy())
        savedmercurydata.append(The_Mercury[0].copy())
        savedvenusdata.append(The_Venus[0].copy())
        savedearthdata.append(The_Earth[0].copy())
        savedmarsdata.append(The_Mars[0].copy())
        savedjupiterdata.append(The_Jupiter[0].copy())
        savedsaturndata.append(The_Saturn[0].copy())
        saveduranusdata.append(The_Uranus[0].copy())
        savedneptunedata.append(The_Neptune[0].copy())
        savedprobeData.append(The_Probe[0].copy())
        savedFlightAngle.append(flight_angle)
        savedSpeed.append(np.linalg.norm(v))
# ============================================================  ##############################
# MERCURY                                                       ###################################
# ============================================================  ########################

Mercury_Distance = 57.91e9       # distance from Sun (m)
The_Mercury_speed = 47.36e3       # orbital velocity (m/s)
Mercury_Angle = -80.57769159743742 + 9.576614667139438e-05 - 8.977670518106606e-08

Mercury_Angle_radian = np.radians(Mercury_Angle)
The_Mercury[0][0] = Mercury_Distance * np.cos(Mercury_Angle_radian)
The_Mercury[0][1] = Mercury_Distance * np.sin(Mercury_Angle_radian)

The_Mercury[1][1] = The_Mercury_speed * np.cos(Mercury_Angle_radian)     
The_Mercury[1][0] = The_Mercury_speed * -np.sin(Mercury_Angle_radian)
  
# ============================================================
# VENUS
# ============================================================

The_Venus[0][0] = 108.21e9        # distance from Sun (m)
The_Venus[1][1] = 35.02e3         # orbital velocity (m/s)


# ============================================================
# EARTH
# ============================================================

The_Earth[0][0] = 149.60e9        # distance from Sun (m)
The_Earth[1][1] = 29.78e3         # orbital velocity (m/s)


# ============================================================
# MARS
# ============================================================

The_Mars[0][0] = 227.92e9         # distance from Sun (m)
The_Mars[1][1] = 24.13e3          # orbital velocity (m/s)


# ============================================================
# JUPITER
# ============================================================

The_Jupiter[0][0] = 778.57e9      # distance from Sun (m)
The_Jupiter[1][1] = 13.06e3       # orbital velocity (m/s)


# ============================================================
# SATURN
# ============================================================

The_Saturn[0][0] = 1.4335e12      # distance from Sun (m)
The_Saturn[1][1] = 9.64e3         # orbital velocity (m/s)


# ============================================================
# URANUS
# ============================================================

The_Uranus[0][0] = 2.8725e12      # distance from Sun (m)
The_Uranus[1][1] = 6.80e3         # orbital velocity (m/s)


# ============================================================
# NEPTUNE
# ============================================================

The_Neptune[0][0] = 4.4951e12     # distance from Sun (m)
The_Neptune[1][1] = 5.43e3        # orbital velocity (m/s)

Run_Time(31536000*time_running,100)




AU = 149e9
Limits = 3

savedmercurydata = np.array(savedmercurydata)
savedvenusdata = np.array(savedvenusdata)
savedearthdata = np.array(savedearthdata)
savedmarsdata = np.array(savedmarsdata)
savedjupiterdata = np.array(savedjupiterdata)
savedsaturndata = np.array(savedsaturndata)
saveduranusdata = np.array(saveduranusdata)
savedneptunedata = np.array(savedneptunedata)

savedprobeData = np.array(savedprobeData)

skip = 100

fig, ax = plt.subplots(figsize=(8, 8))

ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-Limits * AU, Limits * AU)
ax.set_ylim(-Limits * AU, Limits * AU)

mercurytrail, = ax.plot([], [], color='grey', alpha=0.2)
mercurypoint, = ax.plot([], [], 'o')

venustrail, = ax.plot([], [], color='orange', alpha=0.2)
venuspoint, = ax.plot([], [], 'o')

earthtrail, = ax.plot([], [], color='blue', alpha=0.2)
earthpoint, = ax.plot([], [], 'bo')

marstrail, = ax.plot([], [], color='red', alpha=0.2)
marspoint, = ax.plot([], [], 'ro')

jupitertrail, = ax.plot([], [], color='brown', alpha=0.2)
jupiterpoint, = ax.plot([], [], 'o')

saturntrail, = ax.plot([], [], color='gold', alpha=0.2)
saturnpoint, = ax.plot([], [], 'o')

uranustrail, = ax.plot([], [], color='cyan', alpha=0.2)
uranuspoint, = ax.plot([], [], 'o')

neptunetrail, = ax.plot([], [], color='darkblue', alpha=0.2)
neptunepoint, = ax.plot([], [], 'o')

probetrail, = ax.plot([], [], color='red', alpha=0.5)
probepoint, = ax.plot([], [], 'ro')

sun, = ax.plot([],[],'yo',markersize=12)

angleline1, = ax.plot(
    [], [],
    linestyle=':',
    color='grey',
    alpha=0.5
)

def init():

    mercurytrail.set_data([], [])
    mercurypoint.set_data([], [])

    venustrail.set_data([], [])
    venuspoint.set_data([], [])

    earthtrail.set_data([], [])
    earthpoint.set_data([], [])

    marstrail.set_data([], [])
    marspoint.set_data([], [])

    jupitertrail.set_data([], [])
    jupiterpoint.set_data([], [])

    saturntrail.set_data([], [])
    saturnpoint.set_data([], [])

    uranustrail.set_data([], [])
    uranuspoint.set_data([], [])

    neptunetrail.set_data([], [])
    neptunepoint.set_data([], [])

    sun.set_data([],[])
    angleline1.set_data([], [])

    probetrail.set_data([], [])
    probepoint.set_data([], [])

    return (
        mercurytrail, mercurypoint,
        venustrail, venuspoint,
        earthtrail, earthpoint,
        marstrail, marspoint,
        jupitertrail, jupiterpoint,
        saturntrail, saturnpoint,
        uranustrail, uranuspoint,
        neptunetrail, neptunepoint,
        sun, angleline1,
        probetrail, probepoint
    )
probe_end_x = savedprobeData[-1, 0]
probe_end_y = savedprobeData[-1, 1]
angleline1_points =[probe_end_x,probe_end_y]

from matplotlib.patches import Polygon
def update_plane(cross, cube, x, y, angle):
    length = 0.08 * AU
    square_size = 0.025 * AU

    dx = (length / 2) * np.cos(angle)
    dy = (length / 2) * np.sin(angle)

    cross.set_data(
        [x - dx, x + dx],
        [y - dy, y + dy]
    )

    half = square_size / 2

    corners = np.array([
        [-half, -half],
        [ half, -half],
        [ half,  half],
        [-half,  half]
    ])

    rotation = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle),  np.cos(angle)]
    ])

    corners = corners @ rotation.T

    corners[:, 0] += x
    corners[:, 1] += y

    cube.set_xy(corners)

cross1, = ax.plot([], [], '-', linewidth=2, color='black')
Cube1 = Polygon([[0, 0], [0, 0], [0, 0], [0, 0]],
                closed=True, facecolor='black', edgecolor='black')
ax.add_patch(Cube1)

cross2, = ax.plot([], [], '-', linewidth=2, color='black')
Cube2 = Polygon([[0, 0], [0, 0], [0, 0], [0, 0]],
                closed=True, facecolor='black', edgecolor='black')
ax.add_patch(Cube2)

cross3, = ax.plot([], [], '-', linewidth=2, color='black')
Cube3 = Polygon([[0, 0], [0, 0], [0, 0], [0, 0]],
                closed=True, facecolor='black', edgecolor='black')
ax.add_patch(Cube3)

cross4, = ax.plot([], [], '-', linewidth=2, color='black')
Cube4 = Polygon([[0, 0], [0, 0], [0, 0], [0, 0]],
                closed=True, facecolor='black', edgecolor='black')
ax.add_patch(Cube4)

cross5, = ax.plot([], [], '-', linewidth=2, color='black')
Cube5 = Polygon([[0, 0], [0, 0], [0, 0], [0, 0]],
                closed=True, facecolor='black', edgecolor='black')
ax.add_patch(Cube5)

cross6, = ax.plot([], [], '-', linewidth=2, color='black')
Cube6 = Polygon([[0, 0], [0, 0], [0, 0], [0, 0]],
                closed=True, facecolor='black', edgecolor='black')
ax.add_patch(Cube6)

label1 = ax.annotate(
    '',
    xy=(0, 0),
    xytext=(-10, 0),
    textcoords='offset points',
    ha='right',
    va='center',
    fontsize=8*(0.1*Limits)

)

label2 = ax.annotate(
    '',
    xy=(0, 0),
    xytext=(-10, 0),
    textcoords='offset points',
    ha='right',
    va='center',
    fontsize=8*(0.1*Limits)

)

label3 = ax.annotate(
    '',
    xy=(0, 0),
    xytext=(-10, 0),
    textcoords='offset points',
    ha='right',
    va='center',
    fontsize=8*(0.1*Limits)

)

label4 = ax.annotate(
    '',
    xy=(0, 0),
    xytext=(-10, 0),
    textcoords='offset points',
    ha='right',
    va='center',
    fontsize=8*(0.1*Limits)

)

label5 = ax.annotate(
    '',
    xy=(0, 0),
    xytext=(-10, 0),
    textcoords='offset points',
    ha='right',
    va='center',
    fontsize=8*(0.1*Limits)

)
label6 = ax.annotate(
    '',
    xy=(0, 0),
    xytext=(-10, 0),
    textcoords='offset points',
    ha='right',
    va='center',
    fontsize=8*(0.1*Limits)

)
dist2 = savedprobeData[:, 0]**2 + savedprobeData[:, 1]**2

closest_index = np.argmin(dist2)    # point in time the min occurs
closest_to_mercury = np.min(savedProbeMercuryDistance) # the min between probe and mercury

closest_point = savedprobeData[closest_index]
cross1.set_visible(False)
cross2.set_visible(False)
cross3.set_visible(False)
cross4.set_visible(False)
cross5.set_visible(False)
cross6.set_visible(False)
Cube1.set_visible(False)
Cube2.set_visible(False)
Cube3.set_visible(False)
Cube4.set_visible(False)
Cube5.set_visible(False)
Cube6.set_visible(False)

label1.set_visible(False)
label2.set_visible(False)
label3.set_visible(False)
label4.set_visible(False)
label5.set_visible(False)
label6.set_visible(False)

def animate(i):

    index = i * skip

    sun.set_data([0],[0])

    # MERCURY
    mercurytrail.set_data(
        savedmercurydata[:index, 0],
        savedmercurydata[:index, 1]
    )

    mercurypoint.set_data(
        [savedmercurydata[index, 0]],
        [savedmercurydata[index, 1]]
    )


    # VENUS
    venustrail.set_data(
        savedvenusdata[:index, 0],
        savedvenusdata[:index, 1]
    )

    venuspoint.set_data(
        [savedvenusdata[index, 0]],
        [savedvenusdata[index, 1]]
    )


    # EARTH
    earthtrail.set_data(
        savedearthdata[:index, 0],
        savedearthdata[:index, 1]
    )

    earthpoint.set_data(
        [savedearthdata[index, 0]],
        [savedearthdata[index, 1]]
    )


    # MARS
    marstrail.set_data(
        savedmarsdata[:index, 0],
        savedmarsdata[:index, 1]
    )

    marspoint.set_data(
        [savedmarsdata[index, 0]],
        [savedmarsdata[index, 1]]
    )


    # JUPITER
    jupitertrail.set_data(
        savedjupiterdata[:index, 0],
        savedjupiterdata[:index, 1]
    )

    jupiterpoint.set_data(
        [savedjupiterdata[index, 0]],
        [savedjupiterdata[index, 1]]
    )


    # SATURN
    saturntrail.set_data(
        savedsaturndata[:index, 0],
        savedsaturndata[:index, 1]
    )

    saturnpoint.set_data(
        [savedsaturndata[index, 0]],
        [savedsaturndata[index, 1]]
    )


    # URANUS
    uranustrail.set_data(
        saveduranusdata[:index, 0],
        saveduranusdata[:index, 1]
    )

    uranuspoint.set_data(
        [saveduranusdata[index, 0]],
        [saveduranusdata[index, 1]]
    )


    # NEPTUNE
    neptunetrail.set_data(
        savedneptunedata[:index, 0],
        savedneptunedata[:index, 1]
    )

    neptunepoint.set_data(
        [savedneptunedata[index, 0]],
        [savedneptunedata[index, 1]]
    )

    probetrail.set_data(
        savedprobeData[:index, 0],
        savedprobeData[:index, 1]
    )

    probepoint.set_data(
        [savedprobeData[index, 0]],
        [savedprobeData[index, 1]]
    )

    angleline1.set_data(
        [0, angleline1_points[0]],
        [0, angleline1_points[1]]
    )


    #Check
    if index ==0:
        cross1.set_visible(False)
        cross2.set_visible(False)
        cross3.set_visible(False)
        cross4.set_visible(False)
        cross5.set_visible(False)
        cross6.set_visible(False)
        Cube1.set_visible(False)
        Cube2.set_visible(False)
        Cube3.set_visible(False)
        Cube4.set_visible(False)
        Cube5.set_visible(False)
        Cube6.set_visible(False)

        label1.set_visible(False)
        label2.set_visible(False)
        label3.set_visible(False)
        label4.set_visible(False)
        label5.set_visible(False)
        label6.set_visible(False)

    # Checkpoint 1
    if VitalPositions[0] is not None:
        if index >= VitalTickPoints[0]:

            x = VitalPositions[0][0]
            y = VitalPositions[0][1]
            radial_angle = np.arctan2(y, x)

            angle = radial_angle - VitalAngles[0] + np.pi/2

            update_plane(
                cross1,
                Cube1,
                x,
                y,
                angle
            )

            cross1.set_visible(True)
            Cube1.set_visible(True)

            label1.xy = (x, y)

            label1.set_text(
                f"{VitalVelocity[0]:.1f} m s$^{{-1}}$   "
                f"{VitalTempPoints[0]:.1f} K "
                f"{VitalTempSailPoints[0]:.1f} K"
            )

            label1.set_visible(True)

# Checkpoint 2
    if VitalPositions[1] is not None:
        if index >= VitalTickPoints[1]:

            x = VitalPositions[1][0]
            y = VitalPositions[1][1]
            radial_angle = np.arctan2(y, x)
            
            angle = radial_angle - VitalAngles[1] + np.pi/2 

            update_plane(
                cross2,
                Cube2,
                x,
                y,
                angle
            )

            cross2.set_visible(True)
            Cube2.set_visible(True)

            label2.xy = (x, y)

            label2.set_text(
                f"{VitalVelocity[1]:.1f} m s$^{{-1}}$   "
                f"{VitalTempPoints[1]:.1f} K "
                f"{VitalTempSailPoints[1]:.1f} K"
            )

            label2.set_visible(True)
# Checkpoint 3
    if VitalPositions[2] is not None:
        if index >= VitalTickPoints[2]:

            x = VitalPositions[2][0]
            y = VitalPositions[2][1]
            radial_angle = np.arctan2(y, x)
            
            angle = radial_angle - VitalAngles[2] + np.pi/2

            update_plane(
                cross3,
                Cube3,
                x,
                y,
                angle
            )

            cross3.set_visible(True)
            Cube3.set_visible(True)

            label3.xy = (x, y)

            label3.set_text(
                f"{VitalVelocity[2]:.1f} m s$^{{-1}}$   "
                f"{VitalTempPoints[2]:.1f} K "
                f"{VitalTempSailPoints[2]:.1f} K"
            )

            label3.set_visible(True)
# Checkpoint 4
    if VitalPositions[3] is not None:
        if index >= VitalTickPoints[3]:

            x = VitalPositions[3][0]
            y = VitalPositions[3][1]
            radial_angle = np.arctan2(y, x)
            
            angle = radial_angle - VitalAngles[3] + np.pi/2

            update_plane(
                cross4,
                Cube4,
                x,
                y,
                angle
            )

            cross4.set_visible(True)
            Cube4.set_visible(True)

            label4.xy = (x, y)

            label4.set_text(
                f"{VitalVelocity[3]:.1f} m s$^{{-1}}$   "
                f"{VitalTempPoints[3]:.1f} K "
                f"{VitalTempSailPoints[3]:.1f} K"
            )

            label4.set_visible(True)
# Checkpoint 5
    if VitalPositions[4] is not None:
        if index >= VitalTickPoints[4]:

            x = VitalPositions[4][0]
            y = VitalPositions[4][1]
            radial_angle = np.arctan2(y, x)
            
            angle = radial_angle - VitalAngles[4] + np.pi/2

            update_plane(
                cross5,
                Cube5,
                x,
                y,
                angle
            )

            cross5.set_visible(True)
            Cube5.set_visible(True)

            label5.xy = (x, y)

            label5.set_text(
                f"{VitalVelocity[4]:.1f} m s$^{{-1}}$   "
                f"{VitalTempPoints[4]:.1f} K "
                f"{VitalTempSailPoints[4]:.1f} K"
            )

            label5.set_visible(True)

# Checkpoint 6
    if VitalPositions[5] is not None:
        if index >= VitalTickPoints[5]:

            x = VitalPositions[5][0]
            y = VitalPositions[5][1]
            radial_angle = np.arctan2(y, x)
            
            angle = radial_angle - VitalAngles[5] + np.pi/2

            update_plane(
                cross6,
                Cube6,
                x,
                y,
                angle
            )

            cross6.set_visible(True)
            Cube6.set_visible(True)

            label6.xy = (x, y)

            label6.set_text(
                f"{VitalVelocity[5]:.1f} m s$^{{-1}}$   "
                f"{VitalTempPoints[5]:.1f} K "
                f"{VitalTempSailPoints[5]:.1f} K"
            )

            label6.set_visible(True)




    info_text = ax.text(
        0.65, 0.02,
        '',
        transform=ax.transAxes,
        fontsize=7,
        verticalalignment='bottom',
        horizontalalignment='left',
        bbox=dict(
            boxstyle='round,pad=0.3',
            facecolor='white',
            alpha=0
        )
    )
    info_text.set_text(
        f"Escape velocity: {Escape_Velocity:.2f} m s$^{{-1}}$\n \n"
        f"Closest approach: {np.sqrt(dist2[closest_index])/149e9:.5f} AU\n\n"
        f"Estimated time to reach Neptune: {(4.4951e12/Escape_Velocity)/(60*60*24*365):.1f} Yr\n\n"
        f"Estimated time to reach 550 AU: {(82279000000000/Escape_Velocity)/(60*60*24*365):.1f} Yr"
    )
    return (
        sun,angleline1,
        mercurytrail, mercurypoint,
        venustrail, venuspoint,
        earthtrail, earthpoint,
        marstrail, marspoint,
        jupitertrail, jupiterpoint,
        saturntrail, saturnpoint,
        uranustrail, uranuspoint,
        neptunetrail, neptunepoint,
        probetrail,
        probepoint,
        cross1, Cube1,
        cross2, Cube2,
        cross3, Cube3,
        cross4, Cube4,
        cross5, Cube5,
        cross6, Cube6,
        label1,
        label2,
        label3,
        label4,
        label5,
        label6,
        info_text
    )

anim = animation.FuncAnimation(
    fig,
    animate,
    init_func=init,
    frames=len(savedearthdata)//skip,
    interval=1,
    blit=True
)




print("Closest point:", closest_point)
print("Distance:", np.sqrt(dist2[closest_index])/149e9)
print("Angles:")
print(VitalAngles)
print("Main Body Temp:")
print(VitalTempPoints)
print("Sail Temp:")
print(VitalTempSailPoints)
print("Closest approach to mercury:")
print(closest_to_mercury)
print("The angle Difference")
print(Angle_At_Mercury_Flyby_probes-Angle_At_Mercury_Flyby_mercurys)

plt.show()
plt.close(fig)

######################

speed = np.array(savedSpeed)
times = np.arange(len(savedSpeed)) * 100 / Year_Seconds 

plt.plot(times, speed, 'o', label='Data')
plt.xlabel('Time (years)')
plt.ylabel('Speed')
plt.legend()
plt.show()

############################


def reciprocal_power(x, a, b, p, c):
    return c + a / (x + b)**p


y = np.array(sideways_velocity_array)

x = ( Year_Seconds * (2/3) + np.arange(len(y))*100 )

x_fit_data = x - x[0]


p0 = [
    y[0] - y[-1],   
    1,              
    1,              
    y[-1]           
]


step_for_efficiency = 1000

x_fit_sampled = x_fit_data[::step_for_efficiency]
y_sampled = y[::step_for_efficiency]

popt, pcov = curve_fit(
    reciprocal_power,
    x_fit_sampled,
    y_sampled,
    p0=[
        y[0] - y[-1],  
        1,             
        1,             
        y[-1]          
    ],
    bounds=(
        [-np.inf, 0.001, 0.001, -np.inf],
        [ np.inf, np.inf, np.inf,  np.inf]
    ),
    maxfev=50000
)

a, b, p, c = popt


y_pred = reciprocal_power(
    x_fit_data,
    a,
    b,
    p,
    c
)


# R2
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - np.mean(y))**2)

r_squared = 1 - (ss_res / ss_tot)


print("R² =", r_squared)
print("a =", a)
print("b =", b)
print("p =", p)
print("Asymptote =", c)


# Smooth fitted curve
x_fit_relative = np.linspace(
    x_fit_data.min(),
    x_fit_data.max(),
    500
)

y_fit = reciprocal_power(
    x_fit_relative,
    a,
    b,
    p,
    c
)


# Convert fitted x values back to actual time
x_fit_actual = x_fit_relative + x[0]


# Plot
plt.plot(
    x,
    y,
    'o',
    label='Data'
)

plt.plot(
    x_fit_actual,
    y_fit,
    '-',
    label=f'Best fit ($R^2$ = {r_squared:.5f})'
)

Delta_550au = reciprocal_power(
    (82279000000000/Escape_Velocity)-x[0],
    a,
    b,
    p,
    c
)


Delta_2yr = reciprocal_power(
    (Year_Seconds*2)-x[0],
    a,
    b,
    p,
    c
)

plt.plot(
    [x_fit_actual[0], x_fit_actual[-1]],
    [Delta_550au, Delta_550au],
    '-',
    label='Delta V Required at 550 AU'
)

plt.plot(
    [x_fit_actual[0], x_fit_actual[-1]],
    [Delta_2yr, Delta_2yr],
    '-',
    label='Delta V Required after 2 yrs'
)
print("Delta V drift  at  550 AU:")
print(Delta_550au)
print("Delta V drift after 2 yrs:")
print(Delta_2yr)
plt.xlabel("Time (s)")
plt.ylabel("Sideways velocity")
plt.legend()
plt.grid()
plt.show()