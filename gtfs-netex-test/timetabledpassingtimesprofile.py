from netex import ServiceJourney, ServiceJourneyPattern, StopPointInJourneyPattern, TimetabledPassingTime, \
    PointsInJourneyPatternRelStructure, Codespace, TimetabledPassingTimesRelStructure, \
    PointInJourneyPatternRef, ServiceJourneyPatternRef, Call, MultilingualString, RouteView
from refs import getRef, getIndex, getId
import sys

class TimetablePassingTimesProfile:
    codespace: Codespace
    service_journeys: list[ServiceJourney]
    def __init__(self, codespace, version, service_journeys, service_journey_patterns):
        self.codespace = codespace
        # self.version = version
        self.service_journeys = service_journeys
        self.service_journey_patterns = service_journey_patterns

    @staticmethod
    def mapCallToStopPointInJourneyPattern(call: Call) -> StopPointInJourneyPattern:
        stop_point_in_journey_pattern = StopPointInJourneyPattern(
            id=call.id.replace(":Call:", ":StopPointInJourneyPattern:"),
            version=call.version,
            order=call.order,
            derived_from_object_ref=call.id,
            derived_from_version_ref_attribute=call.version
        )
        stop_point_in_journey_pattern.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref = call.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view
        stop_point_in_journey_pattern.for_alighting = call.arrival.for_alighting
        stop_point_in_journey_pattern.for_boarding = call.departure.for_boarding
        stop_point_in_journey_pattern.onward_timing_link_ref = call.onward_timing_link_view
        stop_point_in_journey_pattern.destination_display_ref_or_destination_display_view = call.destination_display_ref_or_destination_display_view
        stop_point_in_journey_pattern.onward_service_link_ref = call.onward_service_link_ref_or_onward_service_link_view  # TODO: select only the service_link_ref
        return stop_point_in_journey_pattern

    @staticmethod
    def mapCallToTimetabledPassingTime(call: Call, pattern: dict) -> TimetabledPassingTime:
        timetabled_passing_time = TimetabledPassingTime(id=call.id.replace(":Call:", ":TimetabledPassingTime:"),
                                                        version=call.version,
                                                        derived_from_object_ref=call.id,
                                                        derived_from_version_ref_attribute=call.version
                                                        )
        timetabled_passing_time.choice_1 = getRef(pattern[call.order])
        timetabled_passing_time.derived_from_object_ref = call.id
        timetabled_passing_time.derived_from_version_ref_attribute = call.version
        timetabled_passing_time.arrival_time = call.arrival.time
        timetabled_passing_time.arrival_day_offset = call.arrival.day_offset
        timetabled_passing_time.departure_time = call.departure.time
        timetabled_passing_time.departure_day_offset = call.departure.day_offset
        return timetabled_passing_time

    @staticmethod
    def sjp_hash(points_in_sequence: PointsInJourneyPatternRelStructure):
        spijp: StopPointInJourneyPattern
        spijp_hash = hash(
            tuple([(spijp.choice.ref, spijp.for_alighting,
                    spijp.for_boarding,
                    spijp.onward_timing_link_ref, spijp.onward_service_link_ref,
                    spijp.destination_display_ref_or_destination_display_view)
                   for spijp in points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern]))
        return ("%0.2X" % (spijp_hash**2))[0:8]

    def getTimetabledPassingTimes(self, force=False, clean=False):
        sjps = {TimetablePassingTimesProfile.sjp_hash(sjp.points_in_sequence): sjp for sjp in self.service_journey_patterns}
        existing_sjps = getIndex(self.service_journey_patterns)

        sj: ServiceJourney
        for sj in self.service_journeys:
            if sj.passing_times and not force:
                if clean:
                    sj.calls = None
                    sj.wait_times = None
                    sj.run_times = None
                    sj.time_demand_type_ref = None
                    sj.time_demand_types = None
                    sj.validity_conditions_or_valid_between = None

                continue

            # if there are calls -> create service journey patterns
            elif sj.calls:
                service_journey_pattern: ServiceJourneyPattern
                service_journey_pattern = None
                if not sj.choice:
                    if len(sj.calls.call) <= 1:
                        print(f"{sj.id} has not enough calls.")
                        pass

                    call: Call
                    spijps = PointsInJourneyPatternRelStructure(
                        point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[self.mapCallToStopPointInJourneyPattern(call) for call in sj.calls.choice])
                    spijp_hash = TimetablePassingTimesProfile.sjp_hash(spijps)

                    """
                    spijp_hash = str(hash(
                        tuple([(spijp.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref.ref, spijp.for_alighting, spijp.for_boarding,
                                spijp.onward_timing_link_ref, spijp.onward_service_link_ref,
                                spijp.destination_display_ref_or_destination_display_view)
                               for spijp in spijps])))
                    """

                    service_journey_pattern = sjps.get(spijp_hash, None)
                    if len(spijps.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern) > 0 and service_journey_pattern is None:
                        service_journey_pattern = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, self.codespace, spijp_hash),
                                                                        version=sj.version,
                                                                        route_ref_or_route_view=RouteView(flexible_line_ref_or_line_ref_or_line_view=sj.choice),
                                                                        name=MultilingualString(value=spijp_hash),
                                                                        derived_from_object_ref = sj.id,
                                                                        derived_from_version_ref_attribute = sj.version,
                                                                        points_in_sequence = spijps)

                        sjps[spijp_hash] = service_journey_pattern

                    sj.choice = getRef(service_journey_pattern, ServiceJourneyPatternRef)
                    # existing_sjps[service_journey_pattern.id] = service_journey_pattern

                elif not service_journey_pattern:
                    service_journey_pattern = existing_sjps[sj.journey_pattern_ref.ref]

                pattern = {x.order: x for x in service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern}

                ttpt = []
                for call in sj.calls.call:
                    # TODO: do something with the different elements of the choice (Call, CallZ, DatedCall, DatedCallZ)
                    pis = pattern[call.order]
                    if pis.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref.ref != call.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view.ref: # TODO: make sure we get the right one
                        print("{} order does not match {} order ({} vs {})".format(service_journey_pattern.id, sj.id,
                                                                                   call.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view,
                                                                                   pis.scheduled_stop_point_ref),
                              file=sys.stderr)

                    else:
                        ttpt.append(self.mapCallToTimetabledPassingTime(call, pattern))

                if len(ttpt) > 0:
                    sj.passing_times = TimetabledPassingTimesRelStructure(timetabled_passing_time=ttpt)

            # if there is a servicejourneypattern, departure time, timedemandtype it can be expanded
            elif sj.choice and sj.departure_time and sj.time_demand_type_ref:
                pass

            # if there are servicejourneypattern, departure time, waittimes, runtimes they can be expanded
            elif sj.choice and sj.departure_time and sj.run_times:
                pass

            if clean:
                sj.calls = None
                sj.wait_times = None
                sj.run_times = None
                sj.time_demand_type_ref = None
                sj.time_demand_types = None
                sj.validity_conditions_or_valid_between = None

        self.service_journey_patterns += sjps.values()