import numpy as np
def detect_feature_drift(reference_data: list, production_data: list, num_bins: int = 10) -> dict:
    """
    Detect feature drift using Population Stability Index (PSI).
    
    Args:
        reference_data: List of feature values from reference distribution (e.g., training)
        production_data: List of feature values from production distribution
        num_bins: Number of bins for histogram comparison
    
    Returns:
        dict with 'psi', 'drift_detected', and 'drift_level'
    """
    if not reference_data or not production_data :
        return {}
    
    if reference_data == production_data :
        return {'psi': 0.0, 'drift_detected': False, 'drift_level': 'none'}
    ref = np.array(reference_data)
    prod = np.array(production_data)
    lo = min(ref.min(),prod.min())
    hi = max(ref.max(),prod.max())
    bins = np.linspace(lo,hi,num_bins+1)
    
    refcount,_ = np.histogram(ref,bins = bins)
    prodcount,_ = np.histogram(prod,bins = bins)
    refcount = refcount / len(reference_data)
    prodcount = prodcount / len(production_data)
    refcount = np.where(refcount ==0,0.0001,refcount)
    prodcount = np.where(prodcount == 0,0.0001,prodcount)

    psi_ = prodcount - refcount
    psi = psi_ * np.log(prodcount/refcount)
    psi = np.sum(psi)
    psi = float(psi)
    psi = round(psi,4)
    drift_detected = False
    drift_level = 'none'
    if psi >= 0.1 :
        drift_detected = True
    
    if psi < 0.1 : 
        drift_level = 'none'
    elif 0.1 <= psi < 0.25 :
        drift_level = 'moderate'
    else:
        drift_level = 'significant'

    return {'psi':psi,'drift_detected':drift_detected,'drift_level':drift_level}
        